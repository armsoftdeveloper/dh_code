import React, { useCallback, useRef ,useState , useEffect } from 'react'
import { SlideNext, SlidePrev } from '../../Img/svg'
import { Swiper, SwiperSlide } from 'swiper/react'
import "swiper/css";
import { EffectCards } from "swiper";
import PageAnim from '../PageAnim/PageAnim';
/***** Axios *****/
import axios from 'axios';
/***** Translation Hook *****/
import { useTranslation } from 'react-i18next';

function Portfolio() {
  const { t, i18n } = useTranslation();
  const [portfolioData, setPortfolioData] = useState([{}]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/dhcode/portfolio/')
      .then(response => {
        setPortfolioData(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  const swiperRef = useRef(null)

  const prevSlide = useCallback(() => {
    swiperRef.current?.swiper.slidePrev();
  }, [swiperRef]);

  const nextSlide = useCallback(() => {
    swiperRef.current?.swiper.slideNext();
  }, [swiperRef]);

  return (
    <>
    <PageAnim />
      <section className="portfolio">
        <div className="portfolio__container">
          <h1>{t("portfolio")}</h1>
          <Swiper
            ref={swiperRef}
            loop={true}
            style={{
              overflow: "unset"
            }}
            className="portfolio__swiper"
            modules={[EffectCards]} effect={"cards"}
          >
            <button className="slideprev" onClick={prevSlide}>
              <SlidePrev />
            </button>
            <button className="slidenext" onClick={nextSlide}>
              <SlideNext />
            </button>
            {
              portfolioData.map(el => (
                <SwiperSlide key={el.id}>
                  <div className='portfolio__item'>
                    <img src={el.img} alt='portfolio' />
                  </div>
                </SwiperSlide>
              ))
            }
          </Swiper>
        </div>
      </section>
    </>

  )
}

export default Portfolio
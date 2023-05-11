import React, { useCallback, useRef , useState , useEffect } from 'react'
import { SlideNext, SlidePrev } from '../../Img/svg'
import { Swiper, SwiperSlide } from 'swiper/react'
import "swiper/css";
import { Pagination, EffectCards } from "swiper";
import PageAnim from '../PageAnim/PageAnim';
/***** Axios *****/
import axios from 'axios';
/***** Translation Hook *****/
import { useTranslation } from 'react-i18next';

function Services() {

  const { t, i18n } = useTranslation();
  const [servicesData, setServicesData] = useState([{}]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/dhcode/services/ru/')
      .then(response => {
        setServicesData(response.data);
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
      <section className="services">
        <div className="services__container">
          <div className="services__title">
            <h2>{t("ourServices")}</h2>
            <div className="btns">
              <button className="slideprev" onClick={prevSlide}>
                <SlidePrev />
              </button>
              <button className="slidenext" onClick={nextSlide}>
                <SlideNext />
              </button>
            </div>
          </div>
          <Swiper
            ref={swiperRef}
            loop={true}
            style={{
              overflow: "unset"
            }}
            className="services__swiper"
            pagination={{
              clickable: true,
            }} modules={[Pagination, EffectCards]} effect={"cards"}
          >
            {
              servicesData.map(el => (
                <SwiperSlide key={el.id}>
                  <div className='services__item'>
                    <h3>{el.title}</h3>
                    <p>{el.description}</p>
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

export default Services
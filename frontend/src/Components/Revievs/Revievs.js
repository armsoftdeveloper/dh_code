import React, { useEffect, useState } from 'react'
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css";
import { Pagination } from "swiper";
import PageAnim from '../PageAnim/PageAnim';
/***** Axios *****/
import axios from 'axios';
/***** Translation Hook *****/
import { useTranslation } from 'react-i18next';

function Revievs() {
  const { t, i18n } = useTranslation();
  const [revievsData, setRevievsData] = useState([{}]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/dhcode/reviews/ru/')
      .then(response => {
        setRevievsData(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  return (
    <>
      <PageAnim />
      <section className="revievs">
        <div className="revievs__container">
          <h1>{t("revievs")}</h1>
          <Swiper
            slidesPerView={"auto"}
            pagination={{
              clickable: true,
            }}
            modules={[Pagination]}
            className="revievs__swiper"
          >
            {
              revievsData.map(el => (
                <SwiperSlide key={el.id}>
                  <div className="revievs__item">
                    <div className="revievs__item-title">
                      <div className="icon">
                        <img src={el.userIcon} alt="asd" />
                      </div>
                      <div className="text">
                        <h4>{el.userName}</h4>
                        <a href={el.href} >Ссылка на сайт</a>
                      </div>
                    </div>
                    <div className="revievs__item-body">
                      <p>{el.body}</p>
                    </div>
                    <div className="revievs__item-bottom">
                      <p>Снимки экрана</p>
                      <div className="flex">
                          <img src={el.img_f} alt='asd' key={el.key}/>
                          <img src={el.img_s} alt='asd' key={el.key}/>
                          <img src={el.img_t} alt='asd' key={el.key}/>
                      </div>
                    </div>
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

export default Revievs
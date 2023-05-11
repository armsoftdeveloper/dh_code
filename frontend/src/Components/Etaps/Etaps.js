import React, { useEffect, useState } from 'react'
import Lottie from 'react-lottie-player'
import IMAGES from '../../Img/img'
import { Swiper, SwiperSlide } from 'swiper/react'
import "swiper/css";
import { EffectCards } from "swiper";
import PageAnim from '../PageAnim/PageAnim';
/***** Axios *****/
import axios from 'axios';
/***** Translation Hook *****/
import { useTranslation } from 'react-i18next';

function Etaps() {

const [etapsData, setEtapsData] = useState([{}]);
const { t, i18n } = useTranslation();

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/dhcode/etaps/ru/')
      .then(response => {
        setEtapsData(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);

  return (
    <>
      <PageAnim />
      <section className="etaps">
        <div className="etaps__container">
          <h2>{t("etaps")}</h2>
          <div className="etaps__flex">
            <div className="swiper-pagination" />
            <div className="lottie-animation">
              <Lottie
                loop
                animationData={IMAGES.lottieAnim}
                play
              />
            </div>
            <div className="etaps__swiper swiper">
              <Swiper
                loop={true}
                style={{
                  overflow: "unset"
                }}
                className="portfolio__swiper"
                modules={[EffectCards]} effect={"cards"}
              >
                {
                  etapsData.map(el => (
                    <SwiperSlide key={el.id}>
                      <div className="etaps__item">
                        <h3>{el.title}</h3>
                        <p>{el.description}</p>
                        <h4>{el.actions_title}</h4>
                        <ul>
                          <li key={el.id}>
                            <p>{el.action_first_title}</p>
                            <p>{el.action_second_title}</p>
                            <p>{el.action_third_title}</p>
                            <p>{el.action_fourth_title}</p>
                            <p>{el.action_fiveth_title}</p>
                          </li>
                        </ul>
                      </div>
                    </SwiperSlide>
                  ))
                }
              </Swiper>
            </div>
          </div>
        </div>
      </section>
    </>
  )
}

export default Etaps
import React, { useEffect, useState } from 'react'
import { MailIcon, PhoneIcon, RuFlag, TgIcon, UsaFlag, WpIcon } from '../../Img/svg'
import IMAGES from '../../Img/img'
import { Link, NavLink } from 'react-router-dom'
import { Swiper, SwiperSlide } from "swiper/react";
import { useTranslation } from 'react-i18next';

import "swiper/css";
/***** Axios *****/
import axios from 'axios';

function Header({lang, setLang}) {
  //Translate Hook 
  const { t, i18n } = useTranslation();

  const [contact, setContact] = useState([{}]);
  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/dhcode/contact/')
      .then(response => {
        setContact(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, []);


  const changeLanguage = (language) => {
    i18n.changeLanguage(language);
  };
  
  const navigationData = [
    {
      id: "1",
      title: t("services"),
      href: "services"
    },
    {
      id: "2",
      title: t("etaps"),
      href: "etaps"
    },
    {
      id: "3",
      title: t("portfolio"),
      href: "portfolio"
    },
    {
      id: "4",
      title: t("benefits"),
      href: "advantages"
    },
    {
      id: "5",
      title: t("revievs"),
      href: "revievs"
    },
    {
      id: "6",
      title: t("contact"),
      href: "contacts"
    },
  ]  
  return (
    <header className="header" id="header">
      <div className="header__container _container">
        <div className="header__left">
          <Link to="/" className="logo">
            <img src={IMAGES.logo} alt="logo" />
          </Link>
          <Swiper
            className="header__swiper"
            slidesPerView={"auto"}
            spaceBetween={10}
          >
            {
              navigationData.map(el => (
                <SwiperSlide key={el.id}>
                  <NavLink to={el.href}>{lang === "RU" ? el.title : el.enTitle}</NavLink>
                </SwiperSlide>
              ))
            }
          </Swiper>
        </div>
        <div className='header__right'>
          <div className="header__contacts">
            <p>{t("comunication")}</p>
            <div className="flex">
              <Link>
                <WpIcon />
              </Link>
              <Link>
                <MailIcon />
              </Link>
              <Link>
                <TgIcon />
              </Link>
              <Link>
                <PhoneIcon />
              </Link>
            </div>
          </div>
          <div className='select-lang'>
            <button onClick={() => changeLanguage('en')}>
            <UsaFlag />
            </button>
            <button onClick={() => changeLanguage('ru')}>
              <RuFlag />
            </button>
          </div>
        </div>
      </div>
    </header>

  )
}

export default Header
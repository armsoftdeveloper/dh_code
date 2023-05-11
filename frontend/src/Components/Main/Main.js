import React, { memo, useEffect, useRef, useState } from 'react'
import { ButtonIcon, Figma, Gulp, Hexagon, Logo, NextJs, NodeJs, Python, ReactJs } from '../../Img/svg';
import IMAGES from '../../Img/img';

/***** Axios *****/
import axios from 'axios';
/***** Translation Hook *****/
import { useTranslation } from 'react-i18next';

function Main() {
  const { t, i18n } = useTranslation();

  const [basic, setBasic] = useState([{}]);
  const hexaagonAnim = useRef(null)
  const mainAnimItem = useRef(null)
  const smallHexagonIcon = useRef(null)
  const impulseAnim = useRef(null)

  let rotate = 0;

  const hexgonInterval = setInterval(function () {
    if (hexaagonAnim !== null) {
      let hexagon = hexaagonAnim.current;
      let animItems = mainAnimItem.current.children
      let logo = hexaagonAnim.current.children[1].children[0];
      let smallHexagon = smallHexagonIcon.current.children[0];
      rotate += 0.3;
      if (rotate >= 360) {
        rotate = 0
      }
      hexagon.style.transform = "rotate(-" + rotate + "deg)"
      logo.style.transform = "rotate(" + rotate + "deg)"
      smallHexagon.style.transform = "rotate(" + rotate + "deg)"
      for (let i = 0; i < animItems.length; i++) {
        animItems[i].style.transform = "rotate(" + rotate + "deg)"
      }
    }
  }, 50)

  const impulsHide = setInterval(function () {
    if(impulseAnim !== null) {
      let impulse = impulseAnim.current.children
      for (let i = 0; i < impulse.length; i++) {
        impulse[i].style.transform = "scale(1.5)"
        impulse[i].style.filter = "blur(0px)"
        impulse[i].style.transition = "all 1s"
      }
    }
  }, 3000)

  const impulsShow = setInterval(function () {
    if(impulseAnim !== null) {
      let impulse = impulseAnim.current.children
      for (let i = 0; i < impulse.length; i++) {
        impulse[i].style.left = Math.round(Math.random() * window.innerWidth) + "px"
        impulse[i].style.top = Math.round(Math.random() * window.innerHeight) + "px"
        impulse[i].style.transform = "scale(0)"
        impulse[i].style.filter = "blur(50px)"
        impulse[i].style.transition = "all 0"
      } 
    }
  }, 2000)

  // useEffect(() => {
  //   axios.get('http://127.0.0.1:8000/api/dhcode/basic/ru/')
  //     .then(response => {
  //       setBasic(response.data);
  //     })
  //     .catch(error => {
  //       console.log(error);
  //     });
  // }, []);

  useEffect(() => {
    return () => {
      clearInterval(impulsShow)
      clearInterval(impulsHide)
      clearInterval(hexgonInterval)
    };
  }, []);

  return (
    <section className="main">
      <video preload="auto" autoPlay loop playsInline muted className="main__bg">
        <source src={IMAGES.mainBg} type="video/mp4" />
      </video>
      <div ref={impulseAnim}>
        <div className='blure-impulse'>
          <Figma />
        </div>
        <div className='blure-impulse'>
          <Gulp />
        </div>
        <div className='blure-impulse'>
          <ReactJs />
        </div>
        <div className='blure-impulse'>
          <NextJs />
        </div>
        <div className='blure-impulse'>
          <Python />
        </div>
        <div className='blure-impulse'>
          <NodeJs />
        </div>
      </div>
      <div className="main__container">
        {basic.map((items,key)=>{
            return (
              <div className="main__text" key={key}>
                <a href="/" className="logo">
                  <img src={IMAGES.logo} alt="logo" />
                </a>
                <h1>{items.title}</h1>
                <p>{items.description}</p>
                <button ref={smallHexagonIcon} >
                  {t("order")}
                  <ButtonIcon />
                </button>
              </div>
            )
          })}
        <div className="main__animation" ref={hexaagonAnim}>
          <div className="hexagon">
            <Hexagon />
          </div>
          <div className="main__animation-logo">
            <Logo />
          </div>
          <div ref={mainAnimItem}>
            <div className="main_animation-item">
              <Figma />
            </div>
            <div className="main_animation-item">
              <Gulp />
            </div>
            <div className="main_animation-item">
              <ReactJs />
            </div>
            <div className="main_animation-item">
              <NextJs />
            </div>
            <div className="main_animation-item">
              <Python />
            </div>
            <div className="main_animation-item">
              <NodeJs />
            </div>
          </div>
        </div>
      </div>
    </section>

  )
}

export default memo(Main)
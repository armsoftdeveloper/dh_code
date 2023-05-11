import React, { useEffect, useState } from 'react'
import PageAnim from '../PageAnim/PageAnim'
/***** Axios *****/
import axios from 'axios';
function Contacts() {
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

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [phone, setPhone] = useState('');
  const [message, setMessage] = useState('');

  const handleNameChange = event => {
    setName(event.target.value);
  }

  const handleEmailChange = event => {
    setEmail(event.target.value);
  }

  const handlePhoneChange = event => {
    setPhone(event.target.value);
  }

  const handleMessageChange = event => {
    setMessage(event.target.value);
  }
  const handleSubmit = (event) => {
    event.preventDefault();
    
    const data = {
      name: name,
      email: email,
      phone: phone,
      message: message,
    }
    axios.post('http://127.0.0.1:8000/api/dhcode/messages/', data)
      .then(response => {
        if(response.status == 200){
          alert("ok")
        }
        else{
          alert("error")
        }
      })
      .catch(error => console.error(error));
    };
  return (
    <>
      <PageAnim />
      <section className="contacts">
        <div className="contacts__container">
          <h1>Контакты</h1>
          <div className="contacts__flex">
            <div className="contacts__map">
              <iframe src="https://yandex.ru/map-widget/v1/?ll=44.491566%2C40.153759&mode=search&ol=geo&ouri=ymapsbm1%3A%2F%2Fgeo%3Fdata%3DCgk3NzIwNDk0NTUSHNWA1aHVtdWh1b3Vv9Wh1bYsINS11oDWh9Wh1bYiCg3bDDJCFeW1IEI%2C&source=entity_search&z=12" />
              <div className="contacts__info">
                <a href="/">fl.ru: hovsepyandavid0</a>
                <a href="/">tg: @d_hovsepyan</a>
                <a href="/">gmail: hovsepyandavid0@gmail.com</a>
                <a href="/">wp: +37441588059</a>
                <a href="/">phone: +37441588059</a>
              </div>
            </div>
            <div className="contacts__form">
              <h3>Оставить заявку</h3>
              <form onSubmit={handleSubmit} method='POST'>
                <label className="input-text">
                  <input type="text" placeholder="name" value={name} onChange={handleNameChange} />
                </label>
                <label className="input-text">
                  <input type="text" placeholder="email" value={email} onChange={handleEmailChange} />
                </label>
                <label className="input-text">
                  <input type="text" placeholder="+ 7 (___) ___ __ __" value={phone} onChange={handlePhoneChange} />
                </label>
                <label className="input-text">
                  <textarea placeholder="message" value={message} onChange={handleMessageChange} />
                </label>
                <label className="input-btn">
                  <input type="submit" defaultValue="Оставить заявку" />
                </label>
              </form>
            </div>
          </div>
        </div>
      </section>
    </>
  )
}

export default Contacts
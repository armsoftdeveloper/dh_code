import React from 'react'
import Header from '../Components/Header/Header'
import { Outlet } from 'react-router-dom'

function HomeWrapper({lang, setLang , pageLanguage , setPageLanguage}) {
  return (
    <>
        <Header {...{lang, setLang}} pageLanguage={pageLanguage} setPageLanguage={setPageLanguage}/>
        <main className='page'>
            <Outlet />
        </main>
    </>
  )
}

export default HomeWrapper
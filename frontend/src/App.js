import { Route, Routes } from 'react-router-dom';
import './App.css';
import "./styles.scss"
import HomeWrapper from './Pages/HomeWrapper';
import Main from './Components/Main/Main';
import Advantages from "./Components/Advantages/Advantages"
import Contacts from './Components/Contacts/Contacts';
import Etaps from './Components/Etaps/Etaps';
import Portfolio from './Components/Portfolio/Portfolio';
import Revievs from './Components/Revievs/Revievs';
import Services from './Components/Services/Services';
import { useState } from 'react';
import { useTranslation } from 'react-i18next';
function App() {

  const { t, i18n } = useTranslation();

  const changeLanguage = (language) => {
    i18n.changeLanguage(language);
  };

  const [lang, setLang] = useState("RU");

  const pageTitle ={
    main: {
      title: "",
      enTitle: ""
    },
    main: {
      title: "",
      enTitle: ""
    },
  }

  return (
    <div className="App">
      <div className='wrapper'>
          <Routes>
            <Route path='/' element={<HomeWrapper {...{lang, setLang}} />}>
              <Route index element={<Main />} />
              <Route path='/advantages' element={<Advantages /> } />
              <Route path='/contacts' element={<Contacts />} />
              <Route path='/etaps' element={<Etaps />} />
              <Route path='/portfolio' element={<Portfolio />} />
              <Route path='/revievs' element={<Revievs />} />
              <Route path='/services' element={<Services />} />
            </Route>
          </Routes>
      </div>
    </div>
    // </I18nextProvider>
  );
}

export default App;

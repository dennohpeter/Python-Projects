from bs4 import BeautifulSoup
page = """
<table class="content_table" border="0" cellspacing="2" cellpadding="3" bgcolor="#4b4b4b">
   <tbody>
      <tr>
         <td class="Caption game_date" align="center" rowspan="2">Date</td>
         <td class="Caption" align="center">FOOTBALL MATCHES</td>
         <td class="Caption prediction_min" align="center" colspan="3">OUTCOME PREDICTION</td>
         <td class="Caption prediction_full" align="center" colspan="5">OUTCOME PREDICTION</td>
         <td class="Caption aver_odds_min" align="center">AVER.<br>ODDS</td>
         <td class="Caption aver_odds_full" align="center" colspan="3">AVERAGE ODDS</td>
         <td class="Caption prediction_min" align="center" rowspan="2" colspan="2" width="47">FT score</td>
         <td class="Caption prediction_full" align="center" rowspan="2" colspan="2" width="47">FT RESULTS</td>
      </tr>
      <tr>
         <td class="Caption" align="center">HOME team - AWAY team</td>
         <td class="Caption prediction_min" width="45" align="center">1X2</td>
         <td class="Caption prediction_full" width="20" align="center">1</td>
         <td class="Caption prediction_full" width="20" align="center">X</td>
         <td class="Caption prediction_full" width="20" align="center">2</td>
         <td class="Caption" width="40" align="center">TIPS</td>
         <td class="Caption" width="35" align="center"></td>
         <td class="Caption prediction_min" width="45" align="center">1X2</td>
         <td class="Caption prediction_full" width="30" align="center">1</td>
         <td class="Caption prediction_full" width="30" align="center">X</td>
         <td class="Caption prediction_full" width="30" align="center">2</td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/10/2019, 23:00');</script>11-03, 02:00
            <noscript>10-03, 23:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-co" title="Colombia Primera A, Apertura" width="16" height="11"> Cucuta Deportivo - Unión Magdalena Santa Marta</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 39%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 25%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 36%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">39%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">36%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.54<br>X: 3.61<br>2: 5.78</td>
         <td class="aver_odds_full" align="center">1.54</td>
         <td class="aver_odds_full" align="center">3.61</td>
         <td class="aver_odds_full" align="center">5.78</td>
         <td align="center">3:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/10/2019, 23:00');</script>11-03, 02:00
            <noscript>10-03, 23:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-mx" title="Mexico Liga de Ascenso, Clausura" width="16" height="11"> Juarez FC - Potros Uaem</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 33%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 36%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 31%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">33%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">36%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">31%</td>
         <td align="center"><font color="green"><b></b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.76<br>X: 3.10<br>2: 4.18</td>
         <td class="aver_odds_full" align="center">1.76</td>
         <td class="aver_odds_full" align="center">3.10</td>
         <td class="aver_odds_full" align="center">4.18</td>
         <td align="center">1:1</td>
         <td bgcolor="Yellow" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/10/2019, 23:00');</script>11-03, 02:00
            <noscript>10-03, 23:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Torneo Federal A" width="16" height="11"> CA Douglas Haig - CD Juventud Unida Gualeguaychu</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">1: 49%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 18%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 33%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">49%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">18%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">33%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center">4</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.80<br>X: 3.25<br>2: 3.70</td>
         <td class="aver_odds_full" align="center">1.80</td>
         <td class="aver_odds_full" align="center">3.25</td>
         <td class="aver_odds_full" align="center">3.70</td>
         <td align="center">2:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/10/2019, 23:00');</script>11-03, 02:00
            <noscript>10-03, 23:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Torneo Federal A" width="16" height="11"> Club Atletico Alvarado - Union de Sunchales</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 26%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 31%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">26%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">31%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.70<br>X: 3.45<br>2: 3.95</td>
         <td class="aver_odds_full" align="center">1.70</td>
         <td class="aver_odds_full" align="center">3.45</td>
         <td class="aver_odds_full" align="center">3.95</td>
         <td align="center">2:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/10/2019, 23:00');</script>11-03, 02:00
            <noscript>10-03, 23:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-pa" title="Panama Liga Panamena de Futbol, Clausura" width="16" height="11"> Santa Gema Fc - Sporting San Miguelito</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 28%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 19%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 54%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">28%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">54%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center">8</td>
         <td class="prob2 aver_odds_min" align="center">1: 3.21<br>X: 3.19<br>2: 1.98</td>
         <td class="aver_odds_full" align="center">3.21</td>
         <td class="aver_odds_full" align="center">3.19</td>
         <td class="aver_odds_full" align="center">1.98</td>
         <td align="center">0:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/10/2019, 23:05');</script>11-03, 02:05
            <noscript>10-03, 23:05</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-" title="Costa Rica Primera Division, Campeonato Verano" width="16" height="11"> Guadelupe FC - Deportivo Saprissa</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 26%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 40%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 33%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">26%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">40%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">33%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 3.89<br>X: 3.34<br>2: 1.77</td>
         <td class="aver_odds_full" align="center">3.89</td>
         <td class="aver_odds_full" align="center">3.34</td>
         <td class="aver_odds_full" align="center">1.77</td>
         <td align="center">0:2</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/10/2019, 23:30');</script>11-03, 02:30
            <noscript>10-03, 23:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-cl" title="Chile Primera Division" width="16" height="11"> Deportes Antofagasta - Curico Unido</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 29%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 28%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 44%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">29%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">28%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">44%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.14<br>X: 3.16<br>2: 3.17</td>
         <td class="aver_odds_full" align="center">2.14</td>
         <td class="aver_odds_full" align="center">3.16</td>
         <td class="aver_odds_full" align="center">3.17</td>
         <td align="center">1:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/10/2019, 23:30');</script>11-03, 02:30
            <noscript>10-03, 23:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-us" title="USA Major League Soccer" width="16" height="11"> Los Angeles FC - Portland Timbers</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 59%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 21%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 19%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">59%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.63<br>X: 4.07<br>2: 4.54</td>
         <td class="aver_odds_full" align="center">1.63</td>
         <td class="aver_odds_full" align="center">4.07</td>
         <td class="aver_odds_full" align="center">4.54</td>
         <td align="center">4:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/10/2019, 23:30');</script>11-03, 02:30
            <noscript>10-03, 23:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ec" title="Ecuador Serie A" width="16" height="11"> Delfin SC - Club Sport Emelec</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 73%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 16%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 11%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">73%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">16%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">11%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.47<br>X: 3.73<br>2: 5.46</td>
         <td class="aver_odds_full" align="center">1.47</td>
         <td class="aver_odds_full" align="center">3.73</td>
         <td class="aver_odds_full" align="center">5.46</td>
         <td align="center">0:0</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/10/2019, 23:30');</script>11-03, 02:30
            <noscript>10-03, 23:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-bo" title="Bolivia Liga Profesional Boliviana, Apertura" width="16" height="11"> Blooming Santa Cruz - The Strongest</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 56%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 17%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 27%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">56%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">17%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">27%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">7</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.02<br>X: 3.46<br>2: 2.90</td>
         <td class="aver_odds_full" align="center">2.02</td>
         <td class="aver_odds_full" align="center">3.46</td>
         <td class="aver_odds_full" align="center">2.90</td>
         <td align="center">2:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/10/2019, 23:45');</script>11-03, 02:45
            <noscript>10-03, 23:45</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-py" title="Paraguay Primera Division, Apertura" width="16" height="11"> Sol de America - Guarani Asuncion</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 25%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 30%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 45%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">30%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">45%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.31<br>X: 3.17<br>2: 2.62</td>
         <td class="aver_odds_full" align="center">2.31</td>
         <td class="aver_odds_full" align="center">3.17</td>
         <td class="aver_odds_full" align="center">2.62</td>
         <td align="center">1:4</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 00:00');</script>11-03, 03:00
            <noscript>11-03, 00:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Primera B Nacional" width="16" height="11"> Mitre Santiago Del Estero - Nueva Chicago</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 28%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 32%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 40%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">28%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">32%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">40%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.13<br>X: 2.84<br>2: 3.34</td>
         <td class="aver_odds_full" align="center">2.13</td>
         <td class="aver_odds_full" align="center">2.84</td>
         <td class="aver_odds_full" align="center">3.34</td>
         <td align="center">1:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 00:30');</script>11-03, 03:30
            <noscript>11-03, 00:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Primera Division, Torneo Inicial" width="16" height="11"> Club Atletico Tucuman - River Plate</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 23%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 31%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 46%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">23%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">31%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">46%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center">5</td>
         <td class="prob2 aver_odds_min" align="center">1: 3.85<br>X: 3.39<br>2: 1.87</td>
         <td class="aver_odds_full" align="center">3.85</td>
         <td class="aver_odds_full" align="center">3.39</td>
         <td class="aver_odds_full" align="center">1.87</td>
         <td align="center">0:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 01:00');</script>11-03, 04:00
            <noscript>11-03, 01:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-co" title="Colombia Primera A, Apertura" width="16" height="11"> America De Cali - Once Caldas S. A.</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">1: 47%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 20%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 33%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">47%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">20%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">33%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center">5</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.02<br>X: 3.03<br>2: 3.63</td>
         <td class="aver_odds_full" align="center">2.02</td>
         <td class="aver_odds_full" align="center">3.03</td>
         <td class="aver_odds_full" align="center">3.63</td>
         <td align="center">3:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 11:30');</script>11-03, 14:30
            <noscript>11-03, 11:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ru" title="Russia Football National League" width="16" height="11"> Spartak 2 - FC Zenit St Petersburg II</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 42%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 17%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 41%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">42%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">17%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">41%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.68<br>X: 3.35<br>2: 4.24</td>
         <td class="aver_odds_full" align="center">1.68</td>
         <td class="aver_odds_full" align="center">3.35</td>
         <td class="aver_odds_full" align="center">4.24</td>
         <td align="center">1:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 14:30');</script>11-03, 17:30
            <noscript>11-03, 14:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ru" title="Russia Premier League" width="16" height="11"> FC Akhmat Grozny - FC Ural Yekaterinburg</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 42%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 35%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 22%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">42%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">35%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">22%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.94<br>X: 2.93<br>2: 4.10</td>
         <td class="aver_odds_full" align="center">1.94</td>
         <td class="aver_odds_full" align="center">2.93</td>
         <td class="aver_odds_full" align="center">4.10</td>
         <td align="center">1:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 15:00');</script>11-03, 18:00
            <noscript>11-03, 15:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ge" title="Georgia National League" width="16" height="11"> FC Wit Georgia Tbilisi - FC Chikhura Sachkhere</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">1: 50%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 19%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 30%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">50%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">30%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center">4</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.11<br>X: 3.01<br>2: 3.10</td>
         <td class="aver_odds_full" align="center">2.11</td>
         <td class="aver_odds_full" align="center">3.01</td>
         <td class="aver_odds_full" align="center">3.10</td>
         <td align="center">1:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 15:30');</script>11-03, 18:30
            <noscript>11-03, 15:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-bg" title="Bulgaria A PFG" width="16" height="11"> Beroe Stara Zagora - FC Vitosha Bistritsa</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 63%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 19%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 19%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">63%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.29<br>X: 4.09<br>2: 9.99</td>
         <td class="aver_odds_full" align="center">1.29</td>
         <td class="aver_odds_full" align="center">4.09</td>
         <td class="aver_odds_full" align="center">9.99</td>
         <td align="center">0:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 15:30');</script>11-03, 18:30
            <noscript>11-03, 15:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ro" title="Romania Liga I" width="16" height="11"> FC Botosani - CS Concordia Chiajna</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 19%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 38%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">38%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.84<br>X: 3.07<br>2: 3.82</td>
         <td class="aver_odds_full" align="center">1.84</td>
         <td class="aver_odds_full" align="center">3.07</td>
         <td class="aver_odds_full" align="center">3.82</td>
         <td align="center">0:0</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 15:30');</script>11-03, 18:30
            <noscript>11-03, 15:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-eg" title="Egypt Premier League" width="16" height="11"> Haras El Hodood - Enppi Club</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 23%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">X: 55%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 22%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">23%</td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">55%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">22%</td>
         <td align="center"><font color="green"><b>X</b></font></td>
         <td align="center">5</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.51<br>X: 2.77<br>2: 2.70</td>
         <td class="aver_odds_full" align="center">2.51</td>
         <td class="aver_odds_full" align="center">2.77</td>
         <td class="aver_odds_full" align="center">2.70</td>
         <td align="center">0:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 15:35');</script>11-03, 18:35
            <noscript>11-03, 15:35</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-world" title="International Clubs AFC Champions League, Group stage" width="16" height="11"> Al Rayyan SC - PFK Lokomotiv Tashkent</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 59%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 19%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 22%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">59%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">22%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">5</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.29<br>X: 3.15<br>2: 2.66</td>
         <td class="aver_odds_full" align="center">2.29</td>
         <td class="aver_odds_full" align="center">3.15</td>
         <td class="aver_odds_full" align="center">2.66</td>
         <td align="center">2:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 16:00');</script>11-03, 19:00
            <noscript>11-03, 16:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-tr" title="Turkey TFF 1. Lig" width="16" height="11"> Denizlispor - Umraniyespor</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 38%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 36%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 26%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">38%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">36%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">26%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.02<br>X: 3.02<br>2: 3.30</td>
         <td class="aver_odds_full" align="center">2.02</td>
         <td class="aver_odds_full" align="center">3.02</td>
         <td class="aver_odds_full" align="center">3.30</td>
         <td align="center">0:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 16:30');</script>11-03, 19:30
            <noscript>11-03, 16:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ru" title="Russia Premier League" width="16" height="11"> FK Krasnodar - FC Gazovik Orenburg</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 69%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 17%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 14%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">69%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">17%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">14%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.54<br>X: 3.60<br>2: 5.82</td>
         <td class="aver_odds_full" align="center">1.54</td>
         <td class="aver_odds_full" align="center">3.60</td>
         <td class="aver_odds_full" align="center">5.82</td>
         <td align="center">2:2</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 17:00');</script>11-03, 20:00
            <noscript>11-03, 17:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-pl" title="Poland Ekstraklasa" width="16" height="11"> Lechia Gdansk - Wisla Plock SA</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 65%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 23%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 12%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">65%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">23%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">12%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.61<br>X: 3.76<br>2: 5.16</td>
         <td class="aver_odds_full" align="center">1.61</td>
         <td class="aver_odds_full" align="center">3.76</td>
         <td class="aver_odds_full" align="center">5.16</td>
         <td align="center">1:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 17:00');</script>11-03, 20:00
            <noscript>11-03, 17:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-cz" title="Czech Republic 1st Liga" width="16" height="11"> Sigma Olmütz - FC Slovan Liberec</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 23%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 32%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 45%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">23%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">32%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">45%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.65<br>X: 2.95<br>2: 2.75</td>
         <td class="aver_odds_full" align="center">2.65</td>
         <td class="aver_odds_full" align="center">2.95</td>
         <td class="aver_odds_full" align="center">2.75</td>
         <td align="center">2:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 17:00');</script>11-03, 20:00
            <noscript>11-03, 17:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-gr" title="Greece Super League" width="16" height="11"> Panetolikos - Panionios</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 38%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 40%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 21%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">38%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">40%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.11<br>X: 2.82<br>2: 3.67</td>
         <td class="aver_odds_full" align="center">2.11</td>
         <td class="aver_odds_full" align="center">2.82</td>
         <td class="aver_odds_full" align="center">3.67</td>
         <td align="center">5:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 17:00');</script>11-03, 20:00
            <noscript>11-03, 17:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-tr" title="Turkey Super Lig" width="16" height="11"> Galatasaray - Antalyaspor AS</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 60%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 15%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 25%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">60%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.26<br>X: 5.41<br>2: 9.17</td>
         <td class="aver_odds_full" align="center">1.26</td>
         <td class="aver_odds_full" align="center">5.41</td>
         <td class="aver_odds_full" align="center">9.17</td>
         <td align="center">5:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 17:00');</script>11-03, 20:00
            <noscript>11-03, 17:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-world" title="International Clubs AFC Cup, Group stage" width="16" height="11"> Nejmeh Beirut - Al Jaish Syr</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 36%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 21%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 43%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">36%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.01<br>X: 2.85<br>2: 3.56</td>
         <td class="aver_odds_full" align="center">2.01</td>
         <td class="aver_odds_full" align="center">2.85</td>
         <td class="aver_odds_full" align="center">3.56</td>
         <td align="center">0:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 17:30');</script>11-03, 20:30
            <noscript>11-03, 17:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-nl" title="Netherlands Beloften Reservecompetitie" width="16" height="11"> Roda JC Kerkrade - SBV Excelsior</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 44%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 15%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 42%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">44%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">42%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.75<br>X: 3.95<br>2: 3.28</td>
         <td class="aver_odds_full" align="center">1.75</td>
         <td class="aver_odds_full" align="center">3.95</td>
         <td class="aver_odds_full" align="center">3.28</td>
         <td align="center">0:3</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 17:30');</script>11-03, 20:30
            <noscript>11-03, 17:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-nl" title="Netherlands Beloften Reservecompetitie" width="16" height="11"> SC Heerenveen - SC Cambuur</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 33%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 15%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 52%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">33%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">52%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center">5</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.81<br>X: 3.79<br>2: 3.18</td>
         <td class="aver_odds_full" align="center">1.81</td>
         <td class="aver_odds_full" align="center">3.79</td>
         <td class="aver_odds_full" align="center">3.18</td>
         <td align="center">2:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 18:00');</script>11-03, 21:00
            <noscript>11-03, 18:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-dk" title="Denmark Superligaen" width="16" height="11"> AGF Aarhus - Odense BK</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 25%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 44%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 32%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">44%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">32%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.94<br>X: 3.26<br>2: 2.21</td>
         <td class="aver_odds_full" align="center">2.94</td>
         <td class="aver_odds_full" align="center">3.26</td>
         <td class="aver_odds_full" align="center">2.21</td>
         <td align="center">1:2</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 18:00');</script>11-03, 21:00
            <noscript>11-03, 18:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-eg" title="Egypt Premier League" width="16" height="11"> Wadi Degla SC - Talaea El Gaish</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 26%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">X: 54%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 20%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">26%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">54%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">20%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center">4</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.28<br>X: 2.88<br>2: 2.91</td>
         <td class="aver_odds_full" align="center">2.28</td>
         <td class="aver_odds_full" align="center">2.88</td>
         <td class="aver_odds_full" align="center">2.91</td>
         <td align="center">0:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 18:00');</script>11-03, 21:00
            <noscript>11-03, 18:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-is" title="Iceland League Cup" width="16" height="11"> Haukar Hafnarfjördur - Breidablik Kopavogur</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 32%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 17%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 51%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">32%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">17%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">51%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center">9</td>
         <td class="prob2 aver_odds_min" align="center">1: 10.97<br>X: 5.99<br>2: 1.15</td>
         <td class="aver_odds_full" align="center">10.97</td>
         <td class="aver_odds_full" align="center">5.99</td>
         <td class="aver_odds_full" align="center">1.15</td>
         <td align="center">1:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-il" title="Israel Premier League" width="16" height="11"> Maccabi Tel Aviv - Bnei Yehuda Tel Aviv</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">X: 49%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 9%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">49%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">9%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.39<br>X: 3.93<br>2: 6.75</td>
         <td class="aver_odds_full" align="center">1.39</td>
         <td class="aver_odds_full" align="center">3.93</td>
         <td class="aver_odds_full" align="center">6.75</td>
         <td align="center">2:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ro" title="Romania Liga I" width="16" height="11"> FC FCSB - FC Viitorul Constanța</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 64%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 21%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 15%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">64%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.80<br>X: 3.20<br>2: 3.82</td>
         <td class="aver_odds_full" align="center">1.80</td>
         <td class="aver_odds_full" align="center">3.20</td>
         <td class="aver_odds_full" align="center">3.82</td>
         <td align="center">1:2</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-be" title="Belgium Reserve League" width="16" height="11"> Sporting Lokeren - RSC Anderlecht</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 9%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 28%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">2: 63%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">9%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">28%</td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">63%</td>
         <td align="center"><font color="green"><b>2</b></font></td>
         <td align="center">4</td>
         <td class="prob2 aver_odds_min" align="center">1: 6.21<br>X: 5.02<br>2: 1.27</td>
         <td class="aver_odds_full" align="center">6.21</td>
         <td class="aver_odds_full" align="center">5.02</td>
         <td class="aver_odds_full" align="center">1.27</td>
         <td align="center">3:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-be" title="Belgium Reserve League" width="16" height="11"> Zulte Waregem - Waasland Beveren</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 13%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 44%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">13%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">44%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.34<br>X: 4.66<br>2: 5.30</td>
         <td class="aver_odds_full" align="center">1.34</td>
         <td class="aver_odds_full" align="center">4.66</td>
         <td class="aver_odds_full" align="center">5.30</td>
         <td align="center">3:5</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-be" title="Belgium Reserve League" width="16" height="11"> KV Oostende - R. Mouscron-Peruwelz</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 28%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 17%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">2: 55%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">28%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">17%</td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">55%</td>
         <td align="center"><font color="green"><b>2</b></font></td>
         <td align="center">6</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.59<br>X: 3.43<br>2: 2.12</td>
         <td class="aver_odds_full" align="center">2.59</td>
         <td class="aver_odds_full" align="center">3.43</td>
         <td class="aver_odds_full" align="center">2.12</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-be" title="Belgium Reserve League" width="16" height="11"> AS Eupen - Royal Charleroi</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 21%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 15%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">2: 63%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">63%</td>
         <td align="center"><font color="green"><b>2</b></font></td>
         <td align="center">4</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.78<br>X: 3.71<br>2: 1.92</td>
         <td class="aver_odds_full" align="center">2.78</td>
         <td class="aver_odds_full" align="center">3.71</td>
         <td class="aver_odds_full" align="center">1.92</td>
         <td align="center">2:0</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 18:30');</script>11-03, 21:30
            <noscript>11-03, 18:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-world" title="International Youth U20 Viareggio Cup" width="16" height="11"> Cagliari - Apia Leichhardt Tigers</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 72%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 7%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 21%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">72%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">7%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.03<br>X: 8.02<br>2: 31.36</td>
         <td class="aver_odds_full" align="center">1.03</td>
         <td class="aver_odds_full" align="center">8.02</td>
         <td class="aver_odds_full" align="center">31.36</td>
         <td align="center">2:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 19:00');</script>11-03, 22:00
            <noscript>11-03, 19:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-nl" title="Netherlands Eerste Divisie" width="16" height="11"> Jong Ajax Amsterdam - Jong AZ Alkmaar</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 63%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 11%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 25%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">63%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">11%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.28<br>X: 5.29<br>2: 7.10</td>
         <td class="aver_odds_full" align="center">1.28</td>
         <td class="aver_odds_full" align="center">5.29</td>
         <td class="aver_odds_full" align="center">7.10</td>
         <td align="center">1:1</td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 19:00');</script>11-03, 22:00
            <noscript>11-03, 19:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-be" title="Belgium Reserve League" width="16" height="11"> Cercle Brugge - KRC Genk</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 22%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 14%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">2: 64%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">22%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">14%</td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">64%</td>
         <td align="center"><font color="green"><b>2</b></font></td>
         <td align="center">9</td>
         <td class="prob2 aver_odds_min" align="center">1: 3.92<br>X: 4.12<br>2: 1.53</td>
         <td class="aver_odds_full" align="center">3.92</td>
         <td class="aver_odds_full" align="center">4.12</td>
         <td class="aver_odds_full" align="center">1.53</td>
         <td align="center">0:1</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 19:00');</script>11-03, 22:00
            <noscript>11-03, 19:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-be" title="Belgium Reserve League" width="16" height="11"> KV Kortrijk - St. Truidense VV</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 64%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 15%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 21%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">64%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">21%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">6</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.88<br>X: 3.87<br>2: 2.77</td>
         <td class="aver_odds_full" align="center">1.88</td>
         <td class="aver_odds_full" align="center">3.87</td>
         <td class="aver_odds_full" align="center">2.77</td>
         <td align="center">1:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 19:00');</script>11-03, 22:00
            <noscript>11-03, 19:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-england" title="England Amateur Premier League 2" width="16" height="11"> Blackburn Rovers - Brighton &amp; Hove Albion</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 41%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 30%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 29%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">41%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">30%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">29%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.79<br>X: 3.52<br>2: 2.10</td>
         <td class="aver_odds_full" align="center">2.79</td>
         <td class="aver_odds_full" align="center">3.52</td>
         <td class="aver_odds_full" align="center">2.10</td>
         <td align="center">2:2</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 19:00');</script>11-03, 22:00
            <noscript>11-03, 19:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-england" title="England Amateur Premier League 2" width="16" height="11"> Norwich City - Stoke City</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 32%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 25%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 43%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">32%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.58<br>X: 3.51<br>2: 2.23</td>
         <td class="aver_odds_full" align="center">2.58</td>
         <td class="aver_odds_full" align="center">3.51</td>
         <td class="aver_odds_full" align="center">2.23</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 19:15');</script>11-03, 22:15
            <noscript>11-03, 19:15</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-de" title="Germany Amateur Regionalliga North" width="16" height="11"> VfB Lubeck - Hamburger SV II</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00ff00" align="center">1: 58%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 16%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 25%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00ff00" align="center">58%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">16%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">25%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center">7</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.56<br>X: 3.66<br>2: 4.84</td>
         <td class="aver_odds_full" align="center">1.56</td>
         <td class="aver_odds_full" align="center">3.66</td>
         <td class="aver_odds_full" align="center">4.84</td>
         <td align="center">2:0</td>
         <td bgcolor="Lime" width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 19:30');</script>11-03, 22:30
            <noscript>11-03, 19:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-de" title="Germany Bundesliga" width="16" height="11"> Fortuna Düsseldorf - Eintracht Frankfurt</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 26%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 33%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 41%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">26%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">33%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">41%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.62<br>X: 3.53<br>2: 2.53</td>
         <td class="aver_odds_full" align="center">2.62</td>
         <td class="aver_odds_full" align="center">3.53</td>
         <td class="aver_odds_full" align="center">2.53</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 19:30');</script>11-03, 22:30
            <noscript>11-03, 19:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-it" title="Italy Serie A" width="16" height="11"> AS Roma - Empoli FC</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 69%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 16%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 15%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">69%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">16%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.55<br>X: 4.29<br>2: 5.24</td>
         <td class="aver_odds_full" align="center">1.55</td>
         <td class="aver_odds_full" align="center">4.29</td>
         <td class="aver_odds_full" align="center">5.24</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 19:45');</script>11-03, 22:45
            <noscript>11-03, 19:45</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-scotland" title="Scotland Premiership" width="16" height="11"> FC St Mirren - Kilmarnock FC</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 38%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 26%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 37%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">38%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">26%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">37%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 4.03<br>X: 3.20<br>2: 1.89</td>
         <td class="aver_odds_full" align="center">4.03</td>
         <td class="aver_odds_full" align="center">3.20</td>
         <td class="aver_odds_full" align="center">1.89</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 19:45');</script>11-03, 22:45
            <noscript>11-03, 19:45</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-fr" title="France Ligue 2" width="16" height="11"> FC Metz - FC Sochaux</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 68%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 19%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 13%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">68%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">13%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.38<br>X: 3.96<br>2: 8.00</td>
         <td class="aver_odds_full" align="center">1.38</td>
         <td class="aver_odds_full" align="center">3.96</td>
         <td class="aver_odds_full" align="center">8.00</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 19:45');</script>11-03, 22:45
            <noscript>11-03, 19:45</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-it" title="Italian amateurs Serie C" width="16" height="11"> AS Gubbio 1910 - Ternana Calcio</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 23%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 34%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">23%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">34%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.53<br>X: 2.81<br>2: 2.64</td>
         <td class="aver_odds_full" align="center">2.53</td>
         <td class="aver_odds_full" align="center">2.81</td>
         <td class="aver_odds_full" align="center">2.64</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 20:00');</script>11-03, 23:00
            <noscript>11-03, 20:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-it" title="Italy Serie B" width="16" height="11"> FBC Unione Venezia - US Palermo</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 20%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">2: 38%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">20%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">38%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 3.08<br>X: 2.99<br>2: 2.32</td>
         <td class="aver_odds_full" align="center">3.08</td>
         <td class="aver_odds_full" align="center">2.99</td>
         <td class="aver_odds_full" align="center">2.32</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 20:00');</script>11-03, 23:00
            <noscript>11-03, 20:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-es" title="Spain Segunda Division" width="16" height="11"> Malaga CF - CA Osasuna</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 35%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">X: 46%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 19%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">35%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">46%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.43<br>X: 2.79<br>2: 3.14</td>
         <td class="aver_odds_full" align="center">2.43</td>
         <td class="aver_odds_full" align="center">2.79</td>
         <td class="aver_odds_full" align="center">3.14</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 20:00');</script>11-03, 23:00
            <noscript>11-03, 20:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Primera D Metropolitana" width="16" height="11"> Deportivo Paraguayo - CA Atlas</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">1: 20%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 30%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 50%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">20%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">30%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">50%</td>
         <td align="center"><font color="green"><b>X2</b></font></td>
         <td align="center">8</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.90<br>X: 2.75<br>2: 2.35</td>
         <td class="aver_odds_full" align="center">2.90</td>
         <td class="aver_odds_full" align="center">2.75</td>
         <td class="aver_odds_full" align="center">2.35</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 20:05');</script>11-03, 23:05
            <noscript>11-03, 20:05</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Primera B Nacional" width="16" height="11"> Arsenal de Sarandi - C</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">1: 46%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 38%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 17%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">46%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">38%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">17%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center">6</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.04<br>X: 2.83<br>2: 3.61</td>
         <td class="aver_odds_full" align="center">2.04</td>
         <td class="aver_odds_full" align="center">2.83</td>
         <td class="aver_odds_full" align="center">3.61</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 20:15');</script>11-03, 23:15
            <noscript>11-03, 20:15</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-pt" title="Portugal Primeira Liga" width="16" height="11"> Benfica Lisbon - CF Os Belenenses</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#00cc00" align="center">1: 78%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 10%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 11%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#00cc00" align="center">78%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">10%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">11%</td>
         <td align="center"><font color="green"><b>1</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 1.15<br>X: 6.85<br>2: 14.65</td>
         <td class="aver_odds_full" align="center">1.15</td>
         <td class="aver_odds_full" align="center">6.85</td>
         <td class="aver_odds_full" align="center">14.65</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 20:30');</script>11-03, 23:30
            <noscript>11-03, 20:30</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-pe" title="Peru Primera Division, Apertura" width="16" height="11"> UTC De Cajamarca - ALIAnza Universidad De Huanuco</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 39%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">X: 47%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 15%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">39%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">47%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">15%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center">10</td>
         <td class="prob2 aver_odds_min" align="center">1: 1.78<br>X: 3.25<br>2: 4.18</td>
         <td class="aver_odds_full" align="center">1.78</td>
         <td class="aver_odds_full" align="center">3.25</td>
         <td class="aver_odds_full" align="center">4.18</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 22:00');</script>12-03, 01:00
            <noscript>11-03, 22:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-ar" title="Argentina Primera Division, Torneo Inicial" width="16" height="11"> CA Tigre - Union de Santa Fe</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 41%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 28%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 30%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">41%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">28%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">30%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 2.46<br>X: 3.02<br>2: 2.85</td>
         <td class="aver_odds_full" align="center">2.46</td>
         <td class="aver_odds_full" align="center">3.02</td>
         <td class="aver_odds_full" align="center">2.85</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#EFEFEF">
         <td>
            <script>mf_usertime('03/11/2019, 22:00');</script>12-03, 01:00
            <noscript>11-03, 22:00</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-mx" title="Mexico Liga MX, Women" width="16" height="11"> Tiburones Rojos De Veracruz - Unam</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">1: 43%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">X: 13%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">2: 45%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">43%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">13%</td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">45%</td>
         <td align="center"><font color="green"><b>12</b></font></td>
         <td align="center"></td>
         <td class="prob2 aver_odds_min" align="center">1: 6.33<br>X: 4.66<br>2: 1.32</td>
         <td class="aver_odds_full" align="center">6.33</td>
         <td class="aver_odds_full" align="center">4.66</td>
         <td class="aver_odds_full" align="center">1.32</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
      <tr bgcolor="#FFFFFF">
         <td>
            <script>mf_usertime('03/11/2019, 22:15');</script>12-03, 01:15
            <noscript>11-03, 22:15</noscript>
            <br>
         </td>
         <td><img src="http://www.zulubet.com/flags/flag-empty.png" class="flags flag-py" title="Paraguay Primera Division, Apertura" width="16" height="11"> Nacional Asuncion - General Diaz</td>
         <td class="prediction_min">
            <table width="100%" border="0" cellspacing="1" cellpadding="0" bgcolor="#000000">
               <tbody>
                  <tr>
                     <td class="prob2" bgcolor="#65ff65" align="center">1: 46%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="#ccfecc" align="center">X: 35%</td>
                  </tr>
                  <tr>
                     <td class="prob2" bgcolor="AliceBlue" align="center">2: 19%</td>
                  </tr>
               </tbody>
            </table>
         </td>
         <td class="prob2 prediction_full" bgcolor="#65ff65" align="center">46%</td>
         <td class="prob2 prediction_full" bgcolor="#ccfecc" align="center">35%</td>
         <td class="prob2 prediction_full" bgcolor="AliceBlue" align="center">19%</td>
         <td align="center"><font color="green"><b>1X</b></font></td>
         <td align="center">6</td>
         <td class="prob2 aver_odds_min" align="center">1: 2.01<br>X: 3.15<br>2: 3.16</td>
         <td class="aver_odds_full" align="center">2.01</td>
         <td class="aver_odds_full" align="center">3.15</td>
         <td class="aver_odds_full" align="center">3.16</td>
         <td align="center"></td>
         <td width="1"></td>
      </tr>
   </tbody>
</table>
"""
page_soup = BeautifulSoup(page, 'lxml')
trs = page_soup.find_all("tr", {'bgcolor': ['#FFFFFF', '#EFEFEF']})
all_games = []
for tr in trs:
    try:
        date, time = tr.select('td > noscript')[0].getText().split(",")
        team = tr.find_all('td')[1].getText().strip()
        tip = tr.select("td > font > b")[0].getText()
        home_team_odd = tr.find_all('td', class_="aver_odds_full")[0].getText().strip()
        draw_odd = tr.find_all('td', class_="aver_odds_full")[1].getText().strip()
        away_odd = tr.find_all('td', class_="aver_odds_full")[2].getText().strip()
        score = tr.find_all('td', align="center")[-1].getText().strip()
        all_games.append([date, time, team, tip, home_team_odd, draw_odd, away_odd, score])
    except IndexError:
        pass
print("\n".join(" ".join(each) for each in all_games))


"""groupings_trial = re.compile(r'''(
                \d+-\d+,\s)                                                       #date
                (\d+:\d+\s)                                                       #time
                ([\w+\W+]*(\s\w+)*\s-\s\w+[^1:]*)              #teams
                ([\d+]*[\s\w+]*1:\s+\d+%)*   #1
                (X:\s+\d+%)*   #X
                (2:\s+\d+%)*   #2
                (\d+%\d+%\d+%)   #
                (12|1X|1|2|X2|X)      #chance
                (\d[^1:])*
                ([1:\s\d+.\d+]+[^X:]*)  #prob1
                (X:\s\d+.\d{2})         #probX
                (2:\s\d+.\d{2})         #prob2
                (\d+.\d+.\d+.\d{2})
                (\d+:\d+|[\s-]*)              #result
                ''', re.VERBOSE) """

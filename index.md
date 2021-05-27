<!-- Begin Jekyll SEO tag v2.7.1 -->
<meta name="generator" content="Jekyll v3.9.0" />
<meta property="og:title" content="Take_out" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Takeout - 초보 연주자를 위한 음원 추출, 음악 추천 프로그램" />
<meta property="og:description" content="Takeout - 초보 연주자를 위한 음원 추출, 음악 추천 프로그램" />
<link rel="canonical" href="https://kookmin-sw.github.io/capstone-2021-10/" />
<!-- <meta property="og:url" content="https://kookmin-sw.github.io/capstone-2021-10/" /> -->
<meta property="og:site_name" content="Take_out" />

<!-- End Jekyll SEO tag -->
  <body>
    <div class="wrapper">
<p><a href="https://kookmin-sw.github.io/capstone-2021-10/"></a>
<img src="https://user-images.githubusercontent.com/28581786/113264752-4916fa80-930e-11eb-868d-557c47967550.png" width="600" /></p>


<h2 id="1.프로젝트 소개">1. 프로젝트소개</h2>
<p>
Take + Out = 음악에서 원하는 소리만 포장해가다.
<br>
연주자가 곡을 연습할 때 악보를 구하지 못하는 경우 여러가지 세션이 섞여있는 음악만 듣고 카피해야 하는 경우가 있습니다. Take out은 효율적인 곡 Copy를 위해 악기별로 들을 수 있도록 최대 5개의 stem을 제공하고, 연주 스타일이 비슷한 종류의 곡을 추천해주는 입문자들을 위한 Web application 입니다.</p>


<h2 id="2.abstract">2. Abstract</h2>
<p>If a player cannot find the score while practicing, he or she may have to listen to and copy only the music that contains a variety of sessions. Takeout is a web application for beginners who recommend similar songs to suit their level, offering up to five items to listen to in each session for efficient song copying.</p>


<h2 id="3.Members">3. Members</h2>
<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>

 - 이효성

   Student ID : 20153218
   E-mail : lho2046@gmail.com
   Role : Leader, Backend, server


 - 유정현

   Student ID : 20151142
   E-mail : dbwjdgus0@kookmin.ac.kr
   Role : Recommend Algorithm, Backend, Data Extraction

 - 김초혜

   Student ID : 20163102
   E-mail : inakplace6666@gmail.com
   Role : Frontend, Data Collection

 - 이윤서

   Student ID : 20171673
   E-mail : westyun1997@gmail.com
   Role : Frontend,Data Collection




</code></pre></div></div>



<h2 id="4. How to Use">4. How to use</h2>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>

<h3>1. youtube 링크를 이용한 사용법<br></h3>
<img width="800" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/youtubelink.png?raw=true"width="800"><br>
1. 원하는 음악의 링크를 가져와서 붙여넣기 합니다.<br>
2. 오른쪽에 Stem 옵션 중 원하는 옵션을 클릭합니다.(2/4/5)<br>
3. Order 버튼을 클릭하여 실행시킵니다.<br>

<img width="800" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/youtubelink_result.png?raw=true"width="800"><br>

실행이 완료되면 해당 사진처럼 결과가 출력되는데<br>
사용자는 원하는 악기를 선택하여 다운로드 하면 됩니다.<br>

<h3>2. 음원 파일을 사용하는 방법</h3>
<img width="800" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/upload2.png?raw=true"width="800"><br>
1. choose a file 버튼을 클릭하여 사용자가 파일을 서버에 업로드 합니다.<br>
2. 오른쪽 Stem 옵션 중 원하는 옵션을 클릭합니다.(2/4/5)<br>
3. Order 버튼을 클릭하여 실행시킵니다.<br>

<img width="800" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/upload_result.png?raw=true"width="800"><br>

실행이 완료되면 해당 사진처럼 결과가 출력되는데<br>
사용자는 원하는 악기를 선택하여 다운로드 하면 됩니다.<br>

<h3>3. 추천시스템 이용 방법</h3>
<img width="800" height="600" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/youtubelink_result.png?raw=true"width="800"><br>
<img width="800" height="600" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/upload_result.png?raw=true"width="800"><br>

위에 사진처럼 작업을 완료한 후 Recommendation 버튼을 누르면 아래 사진처럼 추천 결과 창으로 이동하게 됩니다.<br>

<p><img width="800" src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/recommendation.png?raw=true"></p>

썸네일 아래에 Youtube 링크를 클릭하면 해당 음악의 youtube 페이지로 이동하게 됩니다.<br>
</code></pre></div></div>


<h2 id="4. Data Flow Diagram">4. Data Flow Diagram</h2>
<p><img src="https://github.com/kookmin-sw/capstone-2021-10/blob/master/UIUX/Data%20flow%20diagram_final.png?raw=true" width="800" /></p>

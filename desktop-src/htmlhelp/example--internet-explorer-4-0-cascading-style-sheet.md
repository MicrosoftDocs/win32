---
title: Example Internet Explorer 4.0 Cascading Style Sheet
description: Example Internet Explorer 4.0 Cascading Style Sheet
ms.assetid: 0D22F1CE-640F-4ac0-99A0-E3FD6C94846C
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Example: Internet Explorer 4.0 Cascading Style Sheet


```
/* Cascading Style Sheet for IE4.0 build 1008+ */
body{font-size: 75%; line-height: 125%; font-family: Verdana, Arial, Helvetica,}
a:link{color: #0000FF;}
a:active{color: #FF33CC;}
a:visited{color: #800080;}
h1{font-size:145%;margin-bottom:.5em;}
h2{font-size:125%;margin-top:1.5em;margin-bottom:.5em;}
h3{font-size: 110%;margin-top:1.2em;margin-bottom:.5em;}
p{margin-top:0pt;margin-bottom:0pt;}
li p{margin-top:.6em;margin-bottom:0em;}
big{font-weight:bold;font-size:105%;}
ol{margin-top:.5em;margin-bottom:0em}   
ul{margin-top:.6em;margin-bottom:0em;margin-left:2.75em;}
ol ul{list-style:disc;margin-top:2em;}
li{padding-bottom:.7em;margin-left:-1.25em;}
dl ul{margin-top:2em;margin-bottom:0em;}/*list item inside a def/term*/
dl{margin-top:-1em;}
ol dl{margin-top:-1.5em;margin-left:0em;}/*term/def list inside a numbered list*/
ol dl dl{margin-top: 0em;margin-left:.2em;}/*term/def list inside a term/def list*/
dd{margin-bottom:0em;/*not currently working*/margin-left: 1.5em;}
dt{padding-top:2em;font-weight: bold; margin-left:1.5em;}
code{font-family:Courier;}
pre{margin-top:0em margin-bottom:1.5em; font-family:Courier;   font-size: 125%}
table{font-size:100%;margin-top:1em;margin-bottom:1em;}
th.center{text-align:center;}
th{text-align:left;background:#dddddd;margin: 3pt;vertical-align:bottom;}
tr{vertical-align:top;}
td{margin: 3pt;vertical-align:top;}

/*  IE 4.0 TAGS  */
p.dis{font-size: 6pt;}
h5{}
h5.active{background: #000000;   color: #FFCC99;}

/* -- subheading -- */
h5.subh   {color: #660000;margin-bottom:-1em;margin-top: 1.5em;}

/* -- Overview heading -- */
h5.overh{font-size:120%;margin-bottom:1%;}

/* -- procedure heading -- */
h5.proch{margin-bottom:4pt;}

/* -- topic heading -- */
h5.topich{margin-bottom:-1em;}

/* -- Decision heading -- */
h5.what{color: #993399;margin-bottom:.4em;}

/* -- note 'n' tip heading -- */
h5.note{margin-top:1em;margin-bottom: 0em;}

/* -- related topics heading -- */
h5.relh{margin-top: 2.25em;margin-bottom: -1em;}
```



> [!Note]  
> Because of advances in cascading style sheet technology and specifications, style sheets that work on Microsoft Internet Explorer 4.0 will not work on Internet Explorer 3.02.

 

## Related topics

<dl> <dt>

[About Using Cascading Style Sheets](use-cascading-style-sheets.md)
</dt> </dl>

 

 





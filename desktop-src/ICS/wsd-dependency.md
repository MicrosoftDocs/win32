---
title: WSD Dependency
ms.assetid: 'ac9e4e54-ae7b-40ee-9843-0b94e49dd7b5'
description: 
---

# WSD Dependency

Components may utilize WSD or WSD/WSD event logging in combination. The following are the rules required for WSD:

dir="in" protocol="17" lport="3702" binary="&lt;*YOUR BINARY THAT HOSTS WSD INPROC*&gt;" svc="&lt;*YOUR SERVICE THAT IS HOSTED BY THE BINARY*&gt;"

dir="out" protocol="17" rport="3702" binary="&lt;*YOUR BINARY THAT HOSTS sWSD INPROC*&gt;" svc="&lt;*YOUR SERVICE THAT IS HOSTED BY THE BINARY*&gt;"

If you require WSD event logging then you will need two additional rules:

dir="in" protocol="6" lport="5357" binary="System"

dir="out" protocol="6" rport="5357" binary="System"

 

 





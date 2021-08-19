---
description: Before you begin to develop a Microsoft Windows HTTP Services (WinHTTP) application, you must first decide whether to use the C/C++ API or the COM interface.
ms.assetid: 451ad247-962f-4af1-bb21-0aed4ef5f93c
title: Choosing a WinHTTP Interface
ms.topic: article
ms.date: 05/31/2018
---

# Choosing a WinHTTP Interface

Before you begin to develop a Microsoft Windows HTTP Services (WinHTTP) application, you must first decide whether to use the C/C++ API or the COM interface. The following table summarizes the advantages and disadvantages associated with each of these approaches.




|  | C/C++ API | COM interface | 
|--|-----------|---------------|
| Advantages | <ul><li>Responses can be processed in chunks, which is more efficient.</li><li>POST operations can also be processed in chunks, speeding processing time.</li><li>AutoProxy support.</li><li>Access to the full feature set of WinHTTP.</li><li>Binary data can easily be handled.</li></ul> | <ul><li>Creating an application is easy and requires fewer lines of code than the C/C++ API.</li><li>The interface can be used by scripting languages.</li></ul> | 
| Disadvantages | <ul><li>Processing is more complex.</li><li>The C/C++ API requires more steps than the COM interface to perform the same actions.</li><li>Setting up a request takes more code.</li></ul> | <ul><li>The COM interface does not provide access to the full feature set of WinHTTP.</li><li>It is difficult to handle binary data types in some scripting languages, such as VBScript and JScript.</li><li>The COM interface does not support AutoProxy.</li><li>Applications must use the COM APARTMENT_THREADED model.</li><li>Before a response can begin being processed, the entire response must first be received and buffered.</li></ul> | 




 

 

 




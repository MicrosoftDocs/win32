---
title: The DPC/ISR Action
description: The DPC/ISR Action
ms.assetid: '2f17e1e1-a796-401b-b3b6-7292c734bf46'
---

# The DPC/ISR Action

The DPC/ISR action produces a text report that summarizes the various metrics regarding DPCs and ISRs. The usage for this action is:


```
-a dpcisr [-dpc -isr -summary -interval [n]  -bucket [n] -range T1 T2 ] 
```





| Option                      | Description                                                           |
|-----------------------------|-----------------------------------------------------------------------|
| dpc <br/>             | Show statistics for DPC only <br/>                              |
| isr <br/>             | Show statistics for ISR only <br/>                              |
| summary <br/>         | Show summary report <br/>                                       |
| interval \[dt\] <br/> | Show usage report for intervals of dt, default is 1 second<br/> |
| bucket \[dt\] <br/>   | Show histogram for intervals of dt, default is 2 seconds <br/>  |
| range T1 T2 <br/>     | Show delays between T1 and T2<br/>                              |



 

If no data type is specified, default is to show report for both DPC and ISR. If no report type is specified, default is to print all three kinds of report.

 

 






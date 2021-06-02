---
description: Monitors can be configured using the Network Monitor UI. End-users can pass configuration criteria to your monitor using an HTML form stored as an HTM file in the following sub folder of your installed Network Monitor SDK.
ms.assetid: 7add5984-5bef-431c-a026-06575514397c
title: Monitor Configuration (Network Monitor)
ms.topic: article
ms.date: 05/31/2018
---

# Monitor Configuration (Network Monitor)

Monitors can be configured using the Network Monitor UI. End-users can pass configuration criteria to your monitor using an HTML form stored as an HTM file in the following sub folder of your installed Network Monitor SDK.

``` syntax
%SystemRoot%\System32\Npp\Monitors
```

When an end user selects the **Set Monitor Configuration** button, the browser generates an HTML **POST** message, which includes the names and values for all the HTML form elements.

When the MCSVC calls the [IMonitor::DoConfigure](imonitor-doconfigure.md) method, the *pConfiguration* parameter points to the data from the POST message. The following example code provides an example of POST message data:

``` syntax
ConfigString="FilePath=c%3A%5Ccaptures&StartingNumber=50 \ 
    &EndingNumber=256&MaximumNumberEver=10000 \ 
    &TimeBetweenNotification=120&\
    Addresses=157.54.23.23%0D%0A157.54.23.22% 0D%0A
```

This data is passed in as a long ASCII string. The string looks peculiar, both for its length and the appearance of sections such as %3A%5C and %0D%0A. This peculiarity is caused by HTML, which requires that a method put all possible ANSI, DBCS, and Unicode strings into an ASCII format. For example, the **DoConfigure** method inserts certain characters such as the ampersand (&) in front of each variable name to identify it as a variable name. The %3A%5C is an encoded form of the colon character, and %0D%0A indicates a carriage return/linefeed pair. The following example code provides the resulting HTML code as interpreted by the monitor.

``` syntax
FilePath = c:\captures
StartingNumber=50
EndingNumber = 256
MaximumNumberEver = 10000
TimeBetweenNotification = 120
Addresses= {157.54.23.23, 157.54.23.22}
```

 

 




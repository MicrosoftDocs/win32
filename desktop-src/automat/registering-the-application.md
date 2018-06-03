---
title: Registering the Application
description: Registration maps the ProgID of the application to a unique CLSID, so that you can create instances of the application by name, rather than by CLSID.
ms.assetid: 93375c04-c3cd-44d6-bb9d-3faed4d62282
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering the Application

Registration maps the ProgID of the application to a unique CLSID, so that you can create instances of the application by name, rather than by CLSID. For example, registering Microsoft Excel associates a CLSID with the ProgID Excel.Application.

In Visual Basic, you use the ProgID to create an instance of the application as follows:


```C++
SET xl = CreateObject("Excel.Application")
```



By passing the ProgID to **CLSIDFromProgID**, you can get the corresponding CLSID for use in **CoCreateInstance**. Only applications that will be used in this way need to be registered.

The registration file uses the following syntax for the application:


```C++
\ AppName.ObjectName[.VersionNumber] = human_readable_string
\ AppName.ObjectName\CLSID = {UUID}
```



### Parameters

<dl> <dt>

<span id="AppName"></span><span id="appname"></span><span id="APPNAME"></span>*AppName*
</dt> <dd>

The name of the application.

</dd> <dt>

<span id="ObjectName"></span><span id="objectname"></span><span id="OBJECTNAME"></span>*ObjectName*
</dt> <dd>

The name of the object to be registered (in this case, Application).

</dd> <dt>

<span id="VersionNumber"></span><span id="versionnumber"></span><span id="VERSIONNUMBER"></span>*VersionNumber*
</dt> <dd>

The optional version number of the object.

</dd> <dt>

<span id="human_readable_string"></span><span id="HUMAN_READABLE_STRING"></span>*human\_readable\_string*
</dt> <dd>

A string that describes the application to users. The recommended maximum length is 40 characters.

</dd> <dt>

<span id="UUID"></span><span id="uuid"></span>*UUID*
</dt> <dd>

The universally unique identifier for the application CLSID. To generate a UUID for your class, run the utility Guidgen.exe.

</dd> </dl>

 

 





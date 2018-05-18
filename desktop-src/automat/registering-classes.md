---
title: Registering Classes
description: Objects that can be created with CoCreateInstance must also be registered with the system.
ms.assetid: '30899b2b-8b5b-4923-b0a7-b511e239583a'
---

# Registering Classes

Objects that can be created with **CoCreateInstance** must also be registered with the system. For these objects, registration maps a CLSID to the Automation component file (.dll or .exe) in which the object resides. The CLSID also maps an ActiveX object back to its application and ProgID.

The following figure shows how registration connects ProgIDs, CLSIDs, and ActiveX components.

![](images/oa02-05.png)

The type library can be obtained from its CLSID using the following syntax:


```C++
\CLSID\TypeLib = {UUID of type library}
```



The following syntax indicates that the server is an ActiveX component:


```C++
\CLSID\Programmable 
```



The following shows the resulting example code; these COM class registry keys are required:


```C++
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1} = Hello 2.0 Application
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\ProgID = Hello.Application.2
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\VersionIndependentProgID = Hello.Application
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\LocalServer32 = hello.exe /Automation
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\TypeLib = {F37C8060-4AD5-101B-B826-00DD01103DE1}
HKEY_CLASSES_ROOT\CLSID\{F37C8061-4AD5-101B-B826-00DD01103DE1}\Programmable
```



The registration file uses the following syntax for each class of each object that the application exposes.


```C++
\CLSID\{UUID} = human_readable_string
\CLSID\{UUID}\ProgID = AppName.ObjectName.VersionNumber
\CLSID\{UUID}\VersionIndependentProgID = AppName.ObjectName
\CLSID\{UUID}\LocalServer[32] = filepath[/Automation]
\CLSID\{UUID}\InProcServer[32] = filepath[/Automation]
```



## Parameters

<dl> <dt>

<span id="human_readable_string"></span><span id="HUMAN_READABLE_STRING"></span>*human\_readable\_string*
</dt> <dd>

A string that describes the object to users. The recommended maximum length is 40 characters.

</dd> <dt>

<span id="AppName"></span><span id="appname"></span><span id="APPNAME"></span>*AppName*
</dt> <dd>

The name of the application, as specified previously in the application registration string.

</dd> <dt>

<span id="ObjectName"></span><span id="objectname"></span><span id="OBJECTNAME"></span>*ObjectName*
</dt> <dd>

The name of the object to be registered.

</dd> <dt>

<span id="VersionNumber"></span><span id="versionnumber"></span><span id="VERSIONNUMBER"></span>*VersionNumber*
</dt> <dd>

The version number of the object.

</dd> <dt>

<span id="UUID"></span><span id="uuid"></span>*UUID*
</dt> <dd>

The universally unique identifier for the application CLSID. To generate a UUID for your class, run the utility Guidgen.exe.

</dd> <dt>

<span id="filepath"></span><span id="FILEPATH"></span>*filepath*
</dt> <dd>

The full path and name of the file that contains the object. The optional **/Automation** switch tells the application it was launched for Automation purposes. The switch should be specified for the Application object's class. For more information on **/Automation** see [Initializing the Active Object](lines-sample.md).

</dd> </dl>

## Remarks

The ProgID and VersionIndependentProgID are used by other programmers to gain access to the objects you expose. These identifiers (IDs) should use consistent naming guidelines across all your applications as follows:

-   Can contain up to 39 characters.

-   Must not contain any punctuation (except for the period).

-   Must not start with a digit.

Version-independent names consist of an *AppName*.*ObjectName*, without a version number. For example, Word.Document or Excel.Chart.

Version-dependent names consist of an *AppName*.*ObjectName*.*VersionNumber*, such as Excel.Application.5.

<dl> <dt>

<span id="LocalServer_32__"></span><span id="localserver_32__"></span><span id="LOCALSERVER_32__"></span>LocalServer\[32\] 
</dt> <dd>

Indicates that the ActiveX component is an .exe file and runs in a separate process from the ActiveX client. The optional 32 specifies a server intended for use on 32-bit Windows systems.

</dd> <dt>

<span id="InProcServer_32__"></span><span id="inprocserver_32__"></span><span id="INPROCSERVER_32__"></span>InProcServer\[32\] 
</dt> <dd>

Indicates that the ActiveX component is a DLL and runs in the same process space as the ActiveX client. The optional 32 specifies a server intended for use on 32-bit Windows systems.

The *filepath* you register should give the full path and name. Applications should not rely on the MS-DOS PATH variable to find the object.

</dd> </dl>

 

 





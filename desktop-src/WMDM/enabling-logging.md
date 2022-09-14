---
title: Enabling Logging
description: Enabling Logging
ms.assetid: 50fc1d71-b650-4ba5-a6e1-631c0b9fe8ad
keywords:
- Windows Media Device Manager,logging
- Device Manager,logging
- desktop applications,logging
- service providers,logging
- programming guide,logging
- logging
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Logging

Windows Media Device Manager provides a logging object that can save information to a text file at run time. Developers of both applications and service providers can use this object to store messages in a log file while their application or service provider is running. This object is especially useful when handling DRM-protected files, because Windows Media Device Manager will not allow you to attach a debugger to a process that is handling DRM-protected files.

The logger is a COM object with the class ID CLSID\_WMDMLogger that exposes one interface, [**IWMDMLogger**](/windows/desktop/api/wmdmlog/nn-wmdmlog-iwmdmlogger). Components do not need a certificate to use the logging object.

By default, Windows Media Device Manager maintains a log file, regardless of whether an application uses **IWMDMLogger**. This log file is a simple text file, and each entry includes an entry preceded by a time stamp in the format YYYYMMDDHHMMSS, using 24-hour local time. Windows Media Device Manager logs all API calls, along with any entries you add by calling **IWMDMLogger** messages. All log file entries are appended to the file until [**Reset**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-reset) is called, or the file exceeds its maximum size. The file is closed automatically after each logging operation. The same log file is used for application entries and system entries.

The following steps show how to use the logging object:

1.  Include wmdmlog.h in your project.
2.  Create a logging object by calling **CoCreateInstance**(CLSID\_WMDMLogger) and requesting the **IWMDMLogger** interface. Assign the interface pointer to a global variable.
3.  Verify that logging is enabled by calling [**IWMDMLogger::IsEnabled**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-isenabled); if it is not, enable it by calling [**IWMDMLogger::Enable**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-enable).
4.  Specify a custom log file name and size. This is done by calling [**IWMDMLogger::SetLogFileName**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-setlogfilename) and [**IWMDMLogger::SetSizeParams**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-setsizeparams).
5.  At points in your code where you want to make an entry in the log, call either [**IWMDMLogger::LogDword**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-logdword) to log strings containing variables (this method is similar to **wsprintf** in the way it allows you to format a string containing a variable value), or call [**IWMDMLogger::LogString**](/windows/desktop/api/wmdmlog/nf-wmdmlog-iwmdmlogger-logstring) to log constant strings.

For example code, see the reference pages for the methods of [**IWMDMLogger**](/windows/desktop/api/wmdmlog/nn-wmdmlog-iwmdmlogger).

## Related topics

<dl> <dt>

[**Tasks Common to Applications and Service Providers**](tasks-common-to-applications-and-service-providers.md)
</dt> </dl>

 

 





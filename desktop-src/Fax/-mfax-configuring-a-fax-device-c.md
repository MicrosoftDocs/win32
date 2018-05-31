---
Description: You can configure a fax device programmatically.
ms.assetid: 4800c003-8012-45cd-8bf3-35b7e3d5cd7d
title: Configuring a Fax Device (C++)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configuring a Fax Device (C++)

You can configure a fax device programmatically.

The following C++ code configures a fax device.


```
// The following C++ code configures the first fax device to send faxes and
// automatically receive faxes after 4 rings.
#include <conio.h>
#include <iostream>

// Import the fax service Fxscomex.dll file so that fax service COM objects 
// can be used.
//
// The typical path to fxscomex.dll is shown. 
//
// If this path is not correct, search for fxscomex.dll and replace with 
// the right path.

#import "c:\windows\system32\fxscomex.dll" rename ("GetJob","GetFaxJob") rename ("GetMessage","GetFaxMessage")

using namespace std;

int main ()
{
    try
    {
        HRESULT hr;
        FAXCOMEXLib::IFaxServerPtr sipFaxServer;
        FAXCOMEXLib::IFaxDevicesPtr sipFaxDevices;
        FAXCOMEXLib::IFaxDevicePtr sipFaxDevice;
        //
        //Initialize the COM library on the current thread.
        //
        hr = CoInitialize(NULL); 
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }
        //
        // Connect to the fax server.
        //
        hr = sipFaxServer.CreateInstance("FaxComEx.FaxServer");
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }
        //
        // "" defaults to the machine on which the program is running.
        //
        sipFaxServer -> Connect ("");
        //
        // Get the collection of devices.
        //
        sipFaxDevices = sipFaxServer -> GetDevices();
        //
        // Get the 1st device.
        //
        sipFaxDevice = sipFaxDevices -> GetItem(_variant_t(long(1)));
        //
        // Set the device to answer automatically.
        //
        sipFaxDevice -> ReceiveMode = FAXCOMEXLib::fdrmAUTO_ANSWER;
        //
        // Set the number of rings before the device answers.
        //
        sipFaxDevice -> RingsBeforeAnswer = 4;
        //
        // Enable Send.
        //
        sipFaxDevice -> SendEnabled = VARIANT_TRUE;
        //
        // Save the device configuration.
        //
        sipFaxDevice -> Save();
    }
    catch (_com_error&amp; e)
    {
        cout                                << 
            "Error. HRESULT message is: \"" << 
            e.ErrorMessage()                << 
            "\" ("                          << 
            e.Error()                       << 
            ")"                             << 
            endl;
        if (e.ErrorInfo())
        {
            cout << (char *)e.Description() << endl;
        }
    }
    CoUninitialize();
    return 0;
}
```



 

 




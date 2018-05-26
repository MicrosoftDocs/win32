---
Description: You can create outbound routing rules using C++ programs.
ms.assetid: 56dbd5e4-5c0b-4729-8f19-c03bb78a87c1
title: Creating Outbound Routing Rules (C++)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating Outbound Routing Rules (C++)

You can create [outbound routing rules](-mfax-outbound-routing-rules.md) using C++ programs.

The following C++ code example creates an outbound routing rule. This code will not run on Windows XP Home Edition or Windows XP Professional.


```
// This sample demonstrates how to create an outbound routing rule.
// It creates a rule so that whenever a fax is sent to country/region code 972, 
// area code 4, it is always sent using the first fax device.
// NOTICE: this code will fail if it runs on Windows XP Home Edition or
//         Windows XP Professional. The Fax Outbound Routing Rules exist only
//         in server editions and beyond.

#include <conio.h>
#include <iostream>

//
// Add a rule for country/region code 972 and area code 4.
//
#define COUNTRY_CODE    long(972)
#define AREA_CODE       long(4)

// Import the fax service Fxscomex.dll file so that fax service COM objects 
// can be used.
//
// The typical path to Fxscomex.dll is shown. 
//
// If this path is not correct, search for Fxscomex.dll and replace with 
// the right path.
#import "c:\windows\system32\fxscomex.dll" rename ("GetJob","GetFaxJob") rename ("GetMessage","GetFaxMessage")

using namespace std;

int main ()
{
    try
    {
        HRESULT hr;
        //    
        // Define variables.
        //
        FAXCOMEXLib::IFaxServerPtr sipFaxServer;
        FAXCOMEXLib::IFaxDevicePtr sipFaxDevice;
        FAXCOMEXLib::IFaxDevicesPtr sipFaxDevices;
        FAXCOMEXLib::IFaxOutboundRoutingRulePtr sipFaxOutboundRoutingRule;
        long lID;
        //
        // Initialize the COM library on the current thread.
        //
        hr = CoInitialize(NULL); 
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }
        //
        // Create the root object.
        //
        hr = sipFaxServer.CreateInstance("FaxComEx.FaxServer");
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }
        //
        // Connect to the fax server. 
        // "" defaults to the machine on which the program is running.
        //
        sipFaxServer->Connect("");
        //        
        // Initialize the collection of devices.
        //
        sipFaxDevices = sipFaxServer->GetDevices();
        //
        // Get the first device.
        //
        sipFaxDevice = sipFaxDevices->GetItem(_variant_t(long(1)));
        //
        // Get the device ID.
        //
        lID = sipFaxDevice -> Id;
        //
        // Add a rule.
        //
        sipFaxOutboundRoutingRule = 
            sipFaxServer->OutboundRouting->GetRules()->Add(COUNTRY_CODE,
                                 AREA_CODE,     
                                 VARIANT_TRUE,   // Use device
                                 "",             // Do not care about group name
                                 lID);           // Device ID   
        //
        // Now we can use the newly created rule 
        // through the returned sipFaxOutboundRoutingRule pointer.
        //
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



 

 




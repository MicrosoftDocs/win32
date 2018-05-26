---
Description: The following C++ code tells you the number of incoming, outgoing, routing, and queued messages for the fax server.
ms.assetid: 339a2c79-abf5-4889-a1ca-af1fb213083b
title: Monitoring Fax Activity (C++)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Monitoring Fax Activity (C++)

The following C++ code tells you the number of incoming, outgoing, routing, and queued messages for the fax server.


```
// This sample demonstrates how to monitor fax activity.

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

int main()
{
    try
    {
        HRESULT hr;
        long lQueuedMessages;
        long lIncomingMessages;
        long lOutgoingMessages;
        long lRoutingMessages;
        FAXCOMEXLib::IFaxServerPtr sipFaxServer;
        FAXCOMEXLib::IFaxActivityPtr sipFaxActivity;
        //
        // Initialize the COM library on the current thread.
        //
        hr = CoInitialize(NULL); 
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }

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
        // Initialize the FaxActivity object.
        //
        sipFaxActivity=sipFaxServer->Activity;
        //
        // Get the fax activity properties.
        //
        lIncomingMessages=sipFaxActivity->IncomingMessages;
        lOutgoingMessages=sipFaxActivity->OutgoingMessages;
        lRoutingMessages=sipFaxActivity->RoutingMessages;
        lQueuedMessages=sipFaxActivity->QueuedMessages;
        //
        // Create the output.
        //         
        cout << "Number of incoming messages is " << lIncomingMessages << endl;
        cout << "Number of outgoing messages is " << lOutgoingMessages << endl;
        cout << "Number of routing messages is " << lRoutingMessages << endl;
        cout << "Number of queued messages is " << lQueuedMessages <<endl;
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



 

 




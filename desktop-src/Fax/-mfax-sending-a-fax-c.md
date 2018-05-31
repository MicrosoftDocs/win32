---
Description: 'The following code example sends a fax:'
ms.assetid: a3ab2f07-3e08-4c33-bbb5-1f55b43d8116
title: Sending a Fax (C++)
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sending a Fax (C++)

The following code example sends a fax:


```
// This sample demonstrates how to send a fax.

#include <conio.h>
#include <iostream>

// Import the fax service Fxscomex.dll file so that fax service COM objects 
// can be used.
//
// The typical path to Fxscomex.dll is shown. 
// If this path is not correct, search for Fxscomex.dll and replace with 
// the right path.

#import "c:\windows\system32\fxscomex.dll" rename ("GetJob","GetFaxJob") rename ("GetMessage","GetFaxMessage")

using namespace std;

// You can change properties using the following defines.
#define FAX_BODY                L"c:\\Body.txt"
#define MY_DOCUMENT             L"My First Fax"
#define RECIPIENT_PHONE_NUMBER  L"+1 (425) 555-4567"
#define RECIPIENT_NAME          L"Bill"
#define SENDER_NAME             L"Bob"
#define SENDER_CODE             L"23A54"
#define SENDER_DEPT             L"Accts Payable"
#define SENDER_PHONE_NUMBER     L"+972 (4) 555-9070" 

int main()
{
    try
    {
        HRESULT hr;
        //
        // Define variables.
        //
        FAXCOMEXLib::IFaxServerPtr sipFaxServer;
        FAXCOMEXLib::IFaxActivityPtr sipFaxActivity;
        FAXCOMEXLib::IFaxDocumentPtr sipFaxDocument;
        _variant_t varJobID;
        //
        // Initialize the COM library on the current thread.
        //
        hr = CoInitialize(NULL); 
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }
        //                
        // Create the root objects.
        //
        hr = sipFaxServer.CreateInstance("FaxComEx.FaxServer");
        if (FAILED(hr))
        {
            _com_issue_error(hr);
        }

        hr = sipFaxDocument.CreateInstance("FaxComEx.FaxDocument");
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
        // Set the fax body. 
        //
        sipFaxDocument->Body = FAX_BODY;
        //
        // Name the document.
        //
        sipFaxDocument->DocumentName = MY_DOCUMENT;
        //
        // Add the recipient.
        // 
        sipFaxDocument->Recipients->Add(RECIPIENT_PHONE_NUMBER, RECIPIENT_NAME);
        //
        // To send a fax to more than one recipient, repeat
        // the preceding line for each recipient.
        //
        
        //
        // Set the sender properties.
        //
        sipFaxDocument->Sender->Name = SENDER_NAME;
        sipFaxDocument->Sender->BillingCode = SENDER_CODE;
        sipFaxDocument->Sender->Department = SENDER_DEPT;
        sipFaxDocument->Sender->FaxNumber = SENDER_PHONE_NUMBER;
        //
        // Submit the document to the connected fax server
        // and get back the job ID.
        //
        // Notice we could skip the IFaxServer interface 
        // and use the Submit("") method in this case.
        //
        varJobID = sipFaxDocument->ConnectedSubmit(sipFaxServer);

        long lIndex = 0;
        long lUBound;
        //
        // Get the upper bound of the array or job IDs.
        //
        SafeArrayGetUBound(varJobID.parray, 1, &amp;lUBound);
        for (lIndex = 0; lIndex <= lUBound; lIndex++)
        {
            BSTR bstrJobID;
            SafeArrayGetElement(varJobID.parray , &amp;lIndex, LPVOID(&amp;bstrJobID));
            wprintf (L"Job ID is %s\n", bstrJobID);
        }
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



 

 




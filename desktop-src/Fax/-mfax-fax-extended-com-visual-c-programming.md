---
Description: It is easier for programmers to work with Component Object Model (COM) in certain programming languages than others.
ms.assetid: c918d635-d52c-4ea3-95d6-aa5c9afdbd91
title: Fax Extended COM Visual C++ Programming
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Fax Extended COM Visual C++ Programming

It is easier for programmers to work with Component Object Model (COM) in certain programming languages than others. For example, nearly all the details of using COM are handled implicitly for Microsoft Visual Basic programmers, whereas Microsoft Visual C++ programmers must attend to those details themselves.

The following sections summarize programming details for C and C++ programmers using the fax service extended COM and the [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) directive. It focuses on data types specific to COM (**VARIANT**, **BSTR**, and **SAFEARRAY**), and error handling (\_com\_error).

## Using the \#import Compiler Directive

The [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) Visual C++ compiler directive simplifies working with the fax methods and properties. The directive takes the name of a file containing a type library, such as fxscomex.dll, and generates header files containing typedef declarations, smart pointers for interfaces, and enumerated constants. Each interface is encapsulated, or wrapped, in a class.

For each operation within a class, such as a method or property call, there is a declaration to call the operation directly (that is, the "raw" form of the operation), and a declaration to call the raw operation and throw an exception of the \_com\_error class if the operation fails to execute successfully. If the operation is a property, there is usually a compiler directive that creates an alternative syntax for the operation that has syntax like Visual Basic.

Operations that retrieve the value of a property have names of the form **get\_***Property*. Operations that set the value of a property have names of the form **put\_***Property*. Operations that set the value of a property with a pointer to an fax object have names of the form **putref\_***Property*.

You can get or set a property with calls of these forms:

variable = objectPtr-&gt;get\_*Property*(); // get property value

objectPtr-&gt;put\_*Property*(*value*); // set property value

objectPtr-&gt;putref\_*Property*(&*value*); // set property with object pointer

## Using Property Directives

The **\_\_declspec(property...)** compiler directive is a Microsoft-specific C language extension that declares a function used as a property to have an alternative syntax. As a result, you can set or get values of a property in a way similar to Visual Basic. For example, you can set and get a property as follows:

objectPtr-&gt;*property* = *value*; // set property value

variable = objectPtr-&gt;*property*; // get property value

Notice you do not have to code the following:

objectPtr-&gt;put\_*Property*(*value*); // set property value

variable = objectPtr-&gt;get\_*Property*; // get property value

The compiler will generate the appropriate **get\_***Property*, **put\_***Property*, or **putref\_***Property* call based on what alternative syntax is declared and whether the property is being read or written.

The **\_\_declspec(property...**) compiler directive can only declare **get\_**, **put\_**, or **get\_** and **put\_** alternative syntax for a function. Read-only operations only have a **get\_** declaration; write-only operations only have a **put\_** declaration; operations that are both read and write have both **get\_** and **put\_** declarations.

Only two declarations are possible with this directive; however, each property may have three property functions: **get\_***Property*, **put\_***Property*, or **putref\_***Property*. In that case, only two forms of the property have the alternative syntax.

## Collections, the GetItem Method, and the Item Property

The fax service extended COM defines several collections, such as FaxDevices, FaxInboundRoutingMethods, FaxIncomingJobs, and FaxRecipients. In Visual C++, the **GetItem**(*index*) method returns a member of the collection. Typically, *Index* is a **VARIANT**, the value of which is either a numerical index of the member in the collection, or a string containing the name of the member. In some cases, *Index* is a long value, and will not accept a string.

The **\_\_declspec(property...)** compiler directive declares the **Item** property as an alternative syntax to each collection's fundamental **GetItem()** method. The alternative syntax uses square brackets and looks similar to an array reference. In general, the two forms look like the following:

*collectionPtr*-&gt;GetItem(index);

*collectionPtr*-&gt;Item\[index\];

For example, change the [**RingsBeforeAnswer**](/windows/previous-versions/FaxComex/?branch=master) property of the third device from a collection of devices. Use the **Item()** property to access the third device. This can be expressed in Visual Basic in the following four ways (the last two forms are unique to Visual Basic; other languages do not have equivalents):


```
objFaxDevices.Item(2).RingsBeforeAnswer = 5 
objFaxDevices.Item("My Device Name").RingsBeforeAnswer = 5 
objFaxDevices(2).RingsBeforeAnswer = 5 
objFaxDevices("My Device Name").RingsBeforeAnswer = 5
```



The equivalent in Visual C++ to the first two forms in the preceding example is:


```
objFaxDevices->GetItem(2)->PutRingsBeforeAnswer (5) 
objFaxDevices->GetItem("My Device Name")->PutRingsBeforeAnswer (5)
```



-or- (the alternative syntax for the [**RingsBeforeAnswer**](/windows/previous-versions/FaxComex/?branch=master) property is also shown)


```
objFaxDevices->Item[2]->RingsBeforeAnswer = 5 
objFaxDevices->Item["My Device Name"]->RingsBeforeAnswer = 5
```



## COM-Specific Data Types

In general, any Visual Basic data type you find in the [Fax Service Extended COM Reference](-mfax-fax-service-extended-com-reference.md) has a Visual C++ equivalent. These include standard data types such as **unsigned char** for a Visual Basic **BYTE**, **short** for **short**, and **long** for **LONG**. Look in the syntax blocks of the reference topics to see exactly what is required for the operands of a given method or property.

The exceptions to this rule are the data types specific to COM: **VARIANT**, **BSTR**, and **SAFEARRAY**.

## Variant

A **VARIANT** is a structured data type that contains a value member and a data type member. A **VARIANT** may contain a wide range of other data types including another **VARIANT**, **BSTR**, **BOOL**, [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) or [IUnknown](http://msdn.microsoft.com/en-us/library/ms680509.aspx) pointer, currency, date, and so on. COM also provides methods that make it easy to convert one data type to another.

The **\_variant\_t** class encapsulates and manages the **VARIANT** data type.

When the fax service extended COM reference specifies that a method or property operand takes a value, it usually means the value is passed in a **\_variant\_t**.

This rule is explicitly true when the **Parameters** section in the topics of the fax API reference specifies an operand is a **VARIANT**. One exception is when the documentation explicitly specifies that the operand takes a standard data type, such as **long** or **BYTE**, or an enumeration. Another exception is when the operand takes a **String**.

## BSTR

A **BSTR** (**B**asic **STR**ing) is a structured data type that contains a character string and the string's length. COM provides methods to allocate, manipulate, and free a **BSTR**.

The **\_bstr\_t** class encapsulates and manages the **BSTR** data type.

When the fax service extended COM reference specifies that a method or property takes a **String** value, it means the value is in the form of a **\_bstr\_t**.

Casting **\_variant\_t** and **\_bstr\_t** Classes Often it is not necessary to explicitly code a **\_variant\_t** or **\_bstr\_t** in an argument to an operation. If the **\_variant\_t** or **\_bstr\_t** class has a constructor that matches the data type of the argument, then the compiler will generate the appropriate **\_variant\_t** or **\_bstr\_t**.

However, if the argument is ambiguous, that is, the argument data type matches more than one constructor, you must cast the argument with the appropriate data type to invoke the correct constructor.

## Casting \_variant\_t and \_bstr\_t Classes

Often it is not necessary to explicitly code a **\_variant\_t** or **\_bstr\_t** in an argument to an operation. If the **\_variant\_t** or **\_bstr\_t** class has a constructor that matches the data type of the argument, then the compiler will generate the appropriate **\_variant\_t** or **\_bstr\_t**.

However, if the argument is ambiguous, that is, the argument data type matches more than one constructor, you must cast the argument with the appropriate data type to invoke the correct constructor.

## SafeArray

A **SAFEARRAY** is a structured data type that contains an array of other data types. A **SAFEARRAY** is called safe because it contains information about the bounds of each array dimension, and limits access to array elements within those bounds.

When the fax API reference specifies that a method or property takes or returns an array, it means the method or property takes or returns a **SAFEARRAY**, not a native C/C++ array.

For an example, see [**IFaxDeviceProvider::get\_DeviceIds**](/windows/previous-versions/FaxComex/?branch=master).

## Missing and Default Parameters

Visual Basic allows missing parameters in methods. For example, the [**FaxRecipients**](-mfax-faxrecipients.md) object [**Add**](/windows/previous-versions/FaxComex/nf-faxcomex-ifaxrecipients-add?branch=master) method has two parameters, but you can omit the second parameter (the recipient name). A default **BSTR** or long will be substituted depending on the data type of the missing operand.

In C/C++, all operands must be specified. If you want to specify a missing parameter whose data type is a string, specify a **\_bstr\_t** containing a null string. If you want to specify a missing parameter whose data type is a **VARIANT**, specify a **\_variant\_t** with a value of DISP\_E\_PARAMNOTFOUND and a type of VT\_ERROR. Alternatively, specify the equivalent **\_variant\_t** constant, **vtMissing**, which is supplied by the [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) directive.

## Error Handling

In COM, most operations return an **HRESULT** return code that indicates whether a function completed successfully. The [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) directive generates wrapper code around each "raw" method or property and checks the returned **HRESULT**. If the **HRESULT** indicates failure, the wrapper code generates a COM error by calling \_com\_issue\_errorex() with the **HRESULT** return code as an argument. COM error objects can be caught in a try-catch block. (For efficiency's sake, catch a reference to a \_com\_error object.)

Errors may be errors specific to the fax extended COM, generic [HRESULT](com.error_handling_in_com) errors, or Win32 [system error codes](http://msdn.microsoft.com/library/en-us/debug/base/system_error_codes.asp). Fax-specific errors are described in the topic [Fax Error Codes](-mfax-fax-error-codes.md).

## Visual C++ Equivalents of Visual Basic Conventions

The following is a summary of several conventions in the fax documentation, coded in Visual Basic, as well as their equivalents in Visual C++.

### Declaring a fax Object

In Visual Basic, a fax server object is declared as follows:


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
```



or


```
Dim objFaxServer as FAXCOMEXLib.FaxServer
Set objFaxServer = New FAXCOMEXLib.FaxServer
```



In Visual C++, the [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) directive generates smart pointer-type declarations for all the fax objects. For example, a variable that points to a [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object is of type **IFaxServerPtr**, and is declared as follows:


```
IFaxServerPtr sipFaxServer;
```



A variable that points to a new instance of a [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) object is declared as follows:


```
IFaxServerPtr sipFaxServer; 
hr = sipFaxServer.CreateInstance("FaxComEx.FaxServer");
```



After the **CreateInstance** method is called, the variable can be used as follows:


```
sipFaxServer->Connect("");
```



Notice that in one case, the "." operator is used as if the variable were an instance of a class (sipFaxServer.CreateInstance), and in another case, the "-&gt;" operator is used as if the variable were a pointer to an interface (sipFaxServer-&gt;Connect).

One variable can be used in two ways because the "-&gt;" operator is overloaded to allow an instance of a class to behave like a pointer to an interface. A private class member of the instance variable contains a pointer to the [**FaxServer**](-mfax-faxserver-object-visual-basic-.md) interface; the "-&gt;" operator returns that pointer; and the returned pointer accesses the members of the **FaxServer** object.

### Declaring a Variant

In Visual Basic, a **VARIANT** is declared with the **Dim** statement as follows:

Dim *VariableName* As Variant

In Visual C++, declare a variable as type **\_variant\_t**. A few schematic **\_variant\_t** declarations are shown later in this section.

Note that these declarations provide an idea of what you could code in your own program. For more information, see the examples that follow, and the Visual C++ documentation.

\_variant\_t VariableName(*value*);

\_variant\_t VariableName((*data type cast*) *value*);

\_variant\_t VariableName(*value*, VT\_*DATATYPE*);

\_variant\_t VariableName(interface \* *value*, bool fAddRef = true);

### Using Arrays of Variants

In Visual Basic, arrays of **Variants** can be coded with the **Array** function, or you may use the **Dim** statement, as demonstrated in the following code example, where *JobID* is a variant array:


```
Dim objFaxDocument As New FAXCOMEXLib.FaxDocument
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Dim JobId As Variant

'Set the fax body
objFaxDocument.Body = "c:\Docs\Body.txt"

'Name the document.
objFaxDocument.DocumentName = "My First Fax"

'Add the recipients
With objFaxDocument.Recipients
    .Add ("12225550105")
    .Add ("12225550104")
    .Add ("12225550103")
End with

'Connect to the fax server, submit the document, and get back the 
'job ID array. "" indicates the local server.
JobId = objFaxDocument.Submit("")

'UBound finds the size of the array
For n=0 to UBound(JobID)
    MsgBox "The Job ID is " & JobId(n)
Next n
```



The following Visual C++ code example demonstrates using a **SAFEARRAY** with a **\_variant\_t**.


```
// This sample demonstrates how to send a fax.

#include <conio.h>
#include <iostream>

// Import the fax service Fxscomex.dll file so that fax service COM objects can be used.
// The typical path to Fxscomex.dll is shown. 
// If this path is not correct, search for Fxscomex.dll and replace with the right path.

#import "c:\windows\system32\fxscomex.dll"

using namespace std;

// You can change properties using the following defines.
#define FAX_BODY                L"c:\\Body.txt"
#define MY_DOCUMENT             L"My First Fax"
#define RECIPIENT_PHONE_NUMBER  L"+1 (425) 123-4567"
#define RECIPIENT_NAME          L"Bill"

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
        //*********************************************
        //**
        //** The following illustrates using a 
        //**  SAFEARRAY with a _variant_t.
        //**
        SafeArrayGetUBound(varJobID.parray, 1, &amp;lUBound);
        for (lIndex = 0; lIndex <= lUBound; lIndex++)
        {
            BSTR bstrJobID;
            SafeArrayGetElement(varJobID.parray , &amp;lIndex, LPVOID(&amp;bstrJobID));
            wprintf (L"Job ID is %s\n", bstrJobID);
        }
        //*********************************************
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



### Using Property Get/Put

In Visual Basic, the name of a property is not qualified by whether it is retrieved or assigned.


```
Public Sub GetPut
'Create the root object.
Dim objFaxServer As New FAXCOMEXLib.FaxServer

'Connect to the fax server
objFaxServer.Connect ""

'Set the branding property (put)
objFaxServer.Folders.OutgoingQueue.Branding = False

'Save the change
objFaxServer.Folders.OutgoingQueue.Save

'Display the property (get)
Msgbox objFaxServer.Folders.OutgoingQueue.Branding

End Sub
```



This Visual C++ code example demonstrates **Get/Put***Property*.


```
// This sample demonstrates how to set the branding property.

#include <conio.h>
#include <iostream>

// Import the fax service Fxscomex.dll file so that fax service COM objects can be used.
// The typical path to Fxscomex.dll is shown. 
// If this path is not correct, search for Fxscomex.dll and replace with the right path.

#import "c:\Windows\System32\fxscomex.dll"

using namespace std;

int main()
{
    try
    {
        HRESULT hr;
        //
        // Define variables.
        //
        FAXCOMEXLib::IFaxServerPtr sipFaxServer;
        FAXCOMEXLib::IFaxFoldersPtr sipFaxFolders;
        FAXCOMEXLib::IFaxOutgoingQueuePtr sipFaxOutgoingQueue;
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
        // "" defaults to the machine on which the program is running.
        //
        sipFaxServer -> Connect ("");
        //
        // Initialize the FaxFolders object from the FaxServer object.
        //
        sipFaxFolders = sipFaxServer->Folders;
        //
        // Initialize the FaxOutgoingQueue object from the FaxFolders object.
        //
        sipFaxOutgoingQueue = sipFaxFolders->OutgoingQueue;
        //
        //*********************************************
        //**
        //**  Set the branding property (put)
        //**
        sipFaxOutgoingQueue->Branding = VARIANT_TRUE;
        sipFaxOutgoingQueue->Save();   
        // Display the branding property (get)
        cout << 
            "The branding property has been set to " << 
            ((VARIANT_TRUE == sipFaxOutgoingQueue->Branding) ?
                "TRUE" : "FALSE") << 
            endl;
        //**
        //*********************************************

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



### Using GetItem(x) and Item\[x\]

This Visual Basic code example demonstrates the standard and alternative syntax for **Item()**.


```
Dim objFaxServer As New FAXCOMEXLib.FaxServer
Dim objFaxDevice As FaxDevice
'Connect to the fax server.
objFaxServer.Connect ""
'Get the device.
Set objFaxDevice = objFaxServer.GetDevices.Item(1)
'or
Set objFaxDevice = objFaxServer.GetDevices(1)
objFaxDevice.Description = "Device Number 1"
'Set the device to answer automatically.
objFaxDevice.ReceiveMode = fdrmAUTO_ANSWER
'Set the number of rings before the device answers.
objFaxDevice.RingsBeforeAnswer = 5
'Enable Send
objFaxDevice.SendEnabled = True
 
'Save the device configuration.
objFaxDevice.Save
```



This Visual C++ code example demonstrates **Item**.


```
// The following C++ code configures the first fax device to send faxes and
// automatically receive faxes after 4 rings.

#include <conio.h>
#include <iostream>

// Import the fax service Fxscomex.dll file so that fax service COM objects can be used.
// The typical path to fxscomex.dll is shown. 
// If this path is not correct, search for fxscomex.dll and replace with the right path.

#import "c:\Windows\System32\fxscomex.dll"

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
        //*********************************************
        //
        // Get the 1st device.
        //
        sipFaxDevice = sipFaxDevices -> GetItem(_variant_t(long(1)));
        // or
        sipFaxDevice = sipFaxDevices -> Item[_variant_t(long(1))] ;
        //
        //*********************************************
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



 

 




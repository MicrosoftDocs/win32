---
title: Registering a Callback in Visual Basic
description: Adding a callback in Visual Basic is different from the method used in VBScript.
ms.assetid: 6aebb855-cf5b-4134-b7f6-3a8b404b7ae8
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Callback in Visual Basic

Adding a callback in Visual Basic is different from the method used in VBScript. The **GetRef** function used in VBScript is different than the one used in Visual Basic. Therefore, a developer must create an [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) object that has the callback function as the default method. This topic provides the necessary information to develop Visual Basic applications.

**To implement this callback in an application**

1.  Add references to two object libraries: TLBTypes.olb and VboostTypes6.olb. These object libraries are provided with the Control Point sample code.
2.  Add a reference to Cbklib.tlb. This file defines the structure of the callback function.

    The cbklib.tlb is created using the cbklib.idl file that is included as part of the Control Point sample code. It is recommended that the name of this file change for callback functions that differ in the structure of their parameters. This example uses MIDL to create the type library file.

3.  Write the callback function. The parameters are the same as in the VBScript example in [Registering a Callback](registering-a-callback.md). This example prints a string whenever an event arrives.
    ```VB
    Function eventHandler(ByVal callbackType As Variant, _
    ByVal svcObj As Variant, ByVal varName As Variant, _
    ByVal value As Variant) As Long

        On Error GoTo Error
        'Write some interesting code to do actual work here

        MsgBox "Event Handler Called"
        Exit Function

    Error:
        With Err
            If .Number > 0 Then
                eventHandler = .Number Or &H800A0000
            Else
                eventHandler = .Number
            End If
        End With
    End Function
    ```

    

4.  Add the callback function to the [**IUPnPService**](/windows/desktop/api/Upnp/nn-upnp-iupnpservice) object, as shown in the following example, or in another object such as [**IUPnPDeviceFinder**](/windows/desktop/api/Upnp/nn-upnp-iupnpdevicefinder), using the appropriate callback type library (cbklib.tbl).
    ```VB
    Public Sub AddCbFunction(upnpSvc As UPnPService)

        Dim X As CallbackIUnknownLib.CallBackInterface
        Dim obj As Object
        Dim ptinfo As ITypeInfo
        Dim ptcomp As ITypeComp

        With LoadTypeLibEx(App.Path & "\cbklib.tlb", _
          REGKIND_NONE).GetTypeComp
            .BindType "CallBackInterface", 0, ptinfo, ptcomp
        End With

        'NewDelegator is defined in FunctionDelegator.bas
        Set X = NewDelegator(AddressOf eventHandler) 
        Set obj = CreateStdDispatch(Nothing, ObjPtr(X), ptinfo)
        upnpSvc.AddCallback obj
    End Sub
    ```

    

In the following example, the [**IUPnPService**](/windows/desktop/api/Upnp/nn-upnp-iupnpservice) object is passed to the function. The callback function is then added as the parameter.


```VB
    Dim device as UPnPDevice
    Dim svcObj as UpnPService

    ' Initialize the device using the FindByType or using other methods of finding the devices
    Set svcObj = device.Services("appropriateService")
    Call AddCbFunction(svcObj)
```



## Object Libraries Used in the Sample Code

The previous examples and the Control Point sample code use some of the following object libraries:

1.  TLBTypes.olb — This library defines some of the type library types and interfaces that are used in the sample code. It defines some of the functions to be used in Visual Basic, such as [**LoadTypeLibEx**](/windows/win32/api/oleauto/nf-oleauto-loadtypelibex), that are already available in C or C++.
2.  VboostTypes6.olb — This library defines some base types which are used in TLBTypes.olb and FunctionDelegator.bas. Further information regarding TLBTypes can be found in the book *Advanced Visual Basic 6: Power Techniques for Everyday Programs*, by Matthew Curland (Addison-Wesley, July 2000, ISBN: 0-201-70712-8). (This book may not be available in some languages and countries.)

The Control Point sample code and the following libraries are related to this section and are needed to implement this callback. They can be found with the Control Point sample code:

-   Cbklib.idl
-   Cbklib.tlb
-   VboostTypes6.olb
-   TLBTypes.olb
-   FunctionDelegator.bas

 

 
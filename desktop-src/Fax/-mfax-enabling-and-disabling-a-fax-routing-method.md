---
Description: This topic describes how to enable and disable a fax routing method.
ms.assetid: ce5b63b0-485b-4a57-a7f4-c9feea0f31a0
title: Enabling and Disabling a Fax Routing Method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enabling and Disabling a Fax Routing Method

A fax routing method is an action that is performed each time a fax is received on a port. The fax service executes only the routing methods that have been enabled for the port when it routes an incoming fax transmission.

## In the Win32 Environment

A fax client application can call the [**FaxEnableRoutingMethod**](/windows/previous-versions/Winfax/nf-winfax-faxenableroutingmethoda?branch=master) function to enable a fax routing method for a particular fax device. It can also call the function to disable a routing method enabled by an earlier call to **FaxEnableRoutingMethod** or by the fax service administration application.

To query whether a fax routing method is currently enabled or disabled, an application can call the [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master) function.

Note that an application must first call the [**FaxOpenPort**](/windows/previous-versions/Winfax/nc-winfax-pfaxopenport?branch=master) function to obtain a fax port handle before calling the [**FaxEnableRoutingMethod**](/windows/previous-versions/Winfax/nf-winfax-faxenableroutingmethoda?branch=master) or the [**FaxEnumRoutingMethods**](/windows/previous-versions/Winfax/nf-winfax-faxenumroutingmethodsa?branch=master) functions.

## In the COM Implementation Environment

If you are writing a C/C++ application, you can call the [**IFaxRoutingMethod::put\_Enable**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxroutingmethod-get_enable?branch=master) property method to enable or disable a fax routing method on a specific port. To enable a fax routing method, a fax client application must pass a value of **TRUE** to **IFaxRoutingMethod::put\_Enable**. The **IFaxRoutingMethod::get\_Enable** method retrieves the **Enable** property for a [FaxRoutingMethod](-mfax-faxroutingmethod.md) object. You must retrieve an [IDispatch](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface pointer for a [FaxPort](-mfax-faxport.md) object before you can create a FaxRoutingMethod object. For information about the steps required to create a FaxRoutingMethod object, and for a list of properties and methods, see [**IFaxRoutingMethod**](/windows/previous-versions/Faxcom/nn-faxcom-ifaxroutingmethod?branch=master).

If you are writing a Microsoft Visual Basic application, you can set the [**Enable**](/windows/previous-versions/Faxcom/nf-faxcom-ifaxroutingmethod-get_enable?branch=master) property of the [FaxRoutingMethod](-mfax-faxroutingmethod.md) object to enable or disable a fax routing method on a specific port. If this property is equal to **TRUE**, the routing method is enabled for the port. You must create an instance of a [FaxPort](-mfax-faxport.md) object before you can create a FaxRoutingMethod object. For more information about the steps required to create the object, and for a list of properties and methods of the object, see [**FaxRoutingMethod object (Visual Basic)**](-mfax-faxroutingmethod-object-visual-basic-.md).

 

 




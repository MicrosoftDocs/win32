---
title: Configuring the EAP Method User Interface
description: Explains how to configure the supplicant by supplying an EAP method configuration to EAPHost.
ms.assetid: f6a23201-e221-4098-863f-71a81735d927
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Configuring the EAP Method User Interface

This topic explains how to configure the supplicant by supplying an EAP method configuration to EAPHost.

For a supplicant to perform an EAP-based authentication using EAPHost, a supplicant must supply an EAP method configuration to EAPHost through the [**EapHostPeerBeginSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerbeginsession?branch=master) function.

1.  To obtain the EAP method configuration, a supplicant typically queries EAPHost using [**EapHostPeerGetMethods**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeergetmethods?branch=master) to learn the complete set of EAP methods that are available and installed on the local machine. The list of methods is typically presented to the user in a combination box or other UI control that allows the user to select the method they want.
    > [!Note]  
    > The supplicant may choose to filter the displayed list of methods based on the method property bits indicated in **EAP\_METHOD\_INFO.eapProperties**. Some methods may not be appropriate for the security characteristics of the transport provided by the supplicant, for example.

     

2.  Once the UI control is populated with the set of possible EAP methods, the user selects the method they want to configure. Typically, the supplicant provides a **Configuration** or **Properties** button for the user to access configuration properties of the selected EAP method.
    > [!Note]The supplicant is aware that there are user-configurable properties based on the **eapPropSupportsConfig** bit being enabled in **EAP\_METHOD\_INFO.eapProperties**.
    >
    > For more information, see [**EAP Method Properties**](eap-method-properties.md).

     

3.  When the user clicks the appropriate UI control, the supplicant calls [**EapHostPeerInvokeConfigUI**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeconfigui?branch=master), passing into the function the **HWND** value for the supplicant's own UI, the [**EAP\_METHOD\_TYPE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_type?branch=master) structure obtained from the query to [**EAP\_METHOD\_INFO**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_info?branch=master) structure and other required parameters.
4.  Calling [**EapHostPeerInvokeConfigUI**](/windows/previous-versions/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerinvokeconfigui?branch=master) invokes an EAP method's own configuration UI. On return from **EapHostPeerInvokeConfigUI**, the function will return an EAP method configuration BLOB as an out-parameter.
5.  The supplicant stores the configuration BLOB, along with the [**EAP\_METHOD\_TYPE**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_method_type?branch=master) structure for use with [**EapHostPeerBeginSession**](/windows/previous-versions/eappapis/nf-eappapis-eaphostpeerbeginsession?branch=master).
6.  The precise method for storing the configuraiton BLOB is entirely up to the supplicant. However, the supplicant should always store the configuration in a suitable, secure manner appropriate for system and user authentication configuration data.

## Related topics

<dl> <dt>

[Enabling Group Policy](enabling-group-policy.md)
</dt> <dt>

[Implementing In-Band NAP Support for EAP Methods](enabling-in-band-nap-support.md)
</dt> <dt>

[Implementing NAP Support for EAP Methods](implementing-nap-for-eap-methods.md)
</dt> <dt>

[Transferring Data Between the Supplicant and EAP Methods](transferring-data-between-the-supplicant-and-eap-methods.md)
</dt> <dt>

[EAPHost Supplicants](eaphost-supplicants.md)
</dt> </dl>

 

 





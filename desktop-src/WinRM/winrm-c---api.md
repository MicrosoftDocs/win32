---
title: WinRM C++ API
description: The Windows Remote Management interfaces can be used to obtain data or manage resources on a remote computer. This API is intended primarily for internal use. We recommend using the WinRM Client Shell API instead whenever possible.
ms.assetid: e50075a1-cb43-4bd6-9bbf-6b715fde6a3a
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# WinRM C++ API

The Windows Remote Management interfaces can be used to obtain data or manage [*resources*](windows-remote-management-glossary.md) on a remote computer. This API is intended primarily for internal use. We recommend using the [WinRM Client Shell API](client-shell-api.md) instead whenever possible. The interfaces closely correspond to the [WinRM Scripting API](winrm-scripting-api.md).

The WinRM interfaces that inherit directly from **IDispatch** each have a corresponding scripting object. For more information, see the [WinRM Scripting API](winrm-scripting-api.md).

For multithreaded applications, WinRM does not support separate threads accessing the same [**IWSMAN**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsman) object.

The following interfaces are provided by WinRM.

<dl> <dt>

<span id="IWSMan"></span><span id="iwsman"></span><span id="IWSMAN"></span>[**IWSMan**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsman)
</dt> <dd>

Provides methods and properties used to create a new session and manage an established session. [**WSMan**](wsman.md) is the corresponding scripting object.

</dd> <dt>

<span id="IWSManEx"></span><span id="iwsmanex"></span><span id="IWSMANEX"></span>[**IWSManEx**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsman)
</dt> <dd>

Provides methods and properties used to create a new [**IWSManResourceLocator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanresourcelocator). This method is available for the [**WSMan**](wsman.md) scripting object.

</dd> <dt>

<span id="IWSManConnectionOptions"></span><span id="iwsmanconnectionoptions"></span><span id="IWSMANCONNECTIONOPTIONS"></span>[**IWSManConnectionOptions**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanconnectionoptions)
</dt> <dd>

Defines the user name and password used for remote connections. [**ConnectionOptions**](connectionoptions.md) is the corresponding scripting object.

</dd> <dt>

<span id="IWSManSession"></span><span id="iwsmansession"></span><span id="IWSMANSESSION"></span>[**IWSManSession**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmansession)
</dt> <dd>

Defines the network operations and properties available for the session. [**Session**](session.md) is the corresponding scripting object.

</dd> <dt>

<span id="IWSManEnumerator"></span><span id="iwsmanenumerator"></span><span id="IWSMANENUMERATOR"></span>[**IWSManEnumerator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanenumerator)
</dt> <dd>

Represents a collection of results returned from enumerating a resource. [**Enumerator**](enumerator.md) is the corresponding scripting object.

</dd> <dt>

<span id="IWSManResourceLocator"></span><span id="iwsmanresourcelocator"></span><span id="IWSMANRESOURCELOCATOR"></span>[**IWSManResourceLocator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanresourcelocator)
</dt> <dd>

Supplies the path to a resource. You can use an [**IWSManResourceLocator**](/windows/desktop/api/WSManDisp/nn-wsmandisp-iwsmanresourcelocator) object instead of a [*resource URI*](windows-remote-management-glossary.md) in [**Session**](session.md) object operations. [**ResourceLocator**](resourcelocator.md) is the corresponding scripting object.

</dd> </dl>

## Related topics

<dl> <dt>

[Windows Remote Management Reference](windows-remote-management-reference.md)
</dt> </dl>

 

 





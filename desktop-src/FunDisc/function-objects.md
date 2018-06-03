---
Description: Provides interfaces for discovering function instances and receiving notification events related to changes.
ms.assetid: bdc0cc5c-bec9-419c-ab36-5b05c18f1e82
title: Function Instances
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Function Instances

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Function Discovery provides interfaces for discovering function instances and receiving notification events related to changes.

Function instances are created as the result of a query operation (see [**IFunctionInstanceQuery**](/windows/desktop/api/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancequery)). They represent a static view of a resource at that moment in time.

Function instance collections contain a collection of function instances. These collections support basic enumeration. For more information, see [**IFunctionInstanceCollection**](/windows/desktop/api/FunctionDiscoveryAPI/nn-functiondiscoveryapi-ifunctioninstancecollection).

A function instance exposes the following groups of information:

<dl> <dt>

<span id="identity"></span><span id="IDENTITY"></span>identity
</dt> <dd>

The identity of a function instance uniquely identifies the instance. This identifier is a null-terminated Unicode string. An application can save this string and use it at a later time to find the same resource.

See [**IFunctionInstance::GetID**](/windows/desktop/api/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstance-getid).

</dd> <dt>

<span id="metadata"></span><span id="METADATA"></span>metadata
</dt> <dd>

The metadata represents properties and capabilities. It includes information such as the display name, icon, and installation date. This information is exposed through the **IPropertyStore** interface. Each discovery provider has different capabilities, and so may be able to retrieve different subsets of properties.

See [**IFunctionInstance::OpenPropertyStore**](/windows/desktop/api/FunctionDiscoveryAPI/nf-functiondiscoveryapi-ifunctioninstance-openpropertystore).

</dd> <dt>

<span id="query_service"></span><span id="QUERY_SERVICE"></span>query service
</dt> <dd>

Function instances expose a collection of interfaces that can be used to the device- or resource-specific programming interfaces. Instances only expose interfaces that they directly support. For example, a PnP function instance exposes one or more file paths that can be opened to communicate with the device driver. COM components expose interfaces that the component supports.

See [**IFunctionInstance::QueryService**](/windows/desktop/api/FunctionDiscoveryAPI/).

</dd> </dl>

 

 




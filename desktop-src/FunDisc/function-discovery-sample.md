---
Description: 'Demonstrates the use of Function Discovery API.'
ms.assetid: 'b67e9b53-1c4f-41bf-85bd-d901f3859e92'
title: Function Discovery Sample
---

# Function Discovery Sample

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

The Function Discovery sample demonstrates the use of Function Discovery API. The source code for the sample can be found in the SDK installation location under C:\\Program Files\\Microsoft SDKs\\Windows\\&lt;version number&gt;\\Samples\\winbase\\DeviceFoundation\\FunctionDiscovery\\Client. The Windows Vista SDK is available from the [Download Center](http://go.microsoft.com/fwlink/p/?linkid=102968).

The Function Discovery sample performs the following tasks:

-   Queries the PnP provider for function instances. The [**IFunctionDiscovery::CreateInstanceCollectionQuery**](ifunctiondiscovery-createinstancecollectionquery-method.md) and [**IFunctionInstanceCollectionQuery::Execute**](ifunctioninstancecollectionquery-execute-method.md) methods are used.
-   Displays the list of PnP devices available on the machine. The [**GetCount**](ifunctioninstancecollection-getcount-method.md) and [**Item**](ifunctioninstancecollection-item-method.md) methods of the [**IFunctionInstanceCollection**](ifunctioninstancecollection.md) interface are used.
-   Displays the metadata associated with the device. The [**IFunctionInstance::OpenPropertyStore**](ifunctioninstance-openpropertystore-method.md) method is used.
-   Handles PnP notifications. The [**OnUpdate**](ifunctiondiscoverynotification-onupdate-method.md), [**OnError**](ifunctiondiscoverynotification-onerror.md), and [**OnEvent**](ifunctiondiscoverynotification-onevent.md) methods of the [**IFunctionDiscoveryNotification**](ifunctiondiscoverynotification.md) interface are implemented.

## Related topics

<dl> <dt>

[Using Function Discovery](using-function-discovery.md)
</dt> <dt>

[Using Function Discovery Providers](using-function-discovery-providers.md)
</dt> <dt>

[Function Discovery Provider Sample](function-discovery-provider-sample.md)
</dt> </dl>

 

 




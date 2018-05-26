---
Description: Included with this SDK is sample code that demonstrates the use of the Function Discovery provider API.
ms.assetid: 81955209-d6e2-49a2-ad41-55612b3eb430
title: Function Discovery Provider Sample
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Function Discovery Provider Sample

\[Function Discovery is available for use in the following versions of Windows: Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008, and Windows Vista. It may be altered or unavailable in subsequent versions.\]

Included with this SDK is sample code that demonstrates the use of the Function Discovery provider API. The sample demonstrates how to write a fully functional PnP-X provider by implementing a very simple network protocol. The source code for the sample can be found in the SDK installation location at C:\\Program Files\\Microsoft SDKs\\Windows\\&lt;version number&gt;\\Samples\\winbase\\DeviceFoundation\\FunctionDiscovery\\Provider. The Windows Vista SDK is available from the [Download Center](http://go.microsoft.com/fwlink/p/?linkid=102968).

The Function Discovery provider sample has three components. FDProviderSample.dll contains a COM class that implements the [**IFunctionDiscoveryProvider**](/windows/win32/FunctionDiscoveryProvider/nn-functiondiscoveryprovider-ifunctiondiscoveryprovider?branch=master) interface. FDProviderHostSample.exe implements an executable host for the provider. FDProviderSampleDevice.exe implements a simple soft device that is enumerated by the sample provider. More information about this sample is available in the readme file in the FunctionDiscoveryProvider directory.

The Function Discovery provider sample was developed with the goal of serving as the foundation for implementing providers. It is structured in a way that makes it easy to replace the sample network protocol with a real protocol but preserve the bulk of the code.

To this end, the entire network protocol implementation is contained in DiscoveryProtocol.cpp. TFunctionInstanceInfo is a class that encapsulates all the work of representing the data that represents a device on the network and turns that information into a function instance. The bulk of the work in creating a new provider should be focused on the protocol implementation and in modifying TFunctionInstanceInfo.

Places that require attention during implementation are marked with TODO comments.

The Local System account must have permission to execute files in the folder in which the sample DLL files (such as FDProviderSample.dll) were built.

**To grant folder permissions to the Local Service Account**

1.  Start Windows Explorer.
2.  Browse to the folder in which the sample DLLs were built.
3.  Right-click the folder, click **Properties**, and then click the **Security** tab.
4.  Click **Edit**.
5.  Click **Add**.
6.  Type "LOCAL SERVICE" into the text box, and then click **Check Names**.
7.  Click **OK** to close the next three dialog boxes.

## Related topics

<dl> <dt>

[Using Function Discovery Providers](using-function-discovery-providers.md)
</dt> <dt>

[Function Discovery Sample](function-discovery-sample.md)
</dt> </dl>

 

 




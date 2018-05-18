---
Description: 'You can create the cluster object from script, Visual Basic, C++, or C#.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '00fb8a5c-9879-402d-acfe-15ee5e529f75'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Creating the Cluster Object
---

# Creating the Cluster Object

You can create the cluster object from script, Visual Basic, C++, or C#.

To use this API from C++, use the **\#import** directive to import the Ccpapi.tlb type library. The Ccpapi.tlb type library is included in the CCP SDK and is located in the Microsoft Compute Cluster Pack\\Lib\\i386 or Microsoft Compute Cluster Pack\\Lib\\amd64 folder. To prevent name collisions, also include the rename attributes for the [**ICluster::SetEnvironmentVariable**](icluster-setenvironmentvariable.md), [**ICluster::GetJob**](icluster-getjob.md), and [**ICluster::AddJob**](icluster-addjob.md) methods, as shown in the following C++ example.


```C++
// The Ccpapi.tlb type library is included in the CCP SDK and is 
// located in the Microsoft Compute Cluster Pack\Lib\i386 or \amd64 folder.
// Include the rename attributes to avoid name collisions.
#import "ccpapi.tlb" named_guids no_namespace raw_interfaces_only \
    rename("SetEnvironmentVariable","SetEnvVar") \
    rename("GetJob", "GetSingleJob") \
    rename("AddJob", "AddSingleJob")
```



To create an instance of the cluster object in C++, call the [**CoCreateInstance**](_com_cocreateinstance) function. Use CLSID\_Cluster as the class identifier and IID\_ICluster as the interface identifier. The following C++ example shows how to create an instance of the Cluster object.


```C++
HRESULT hr = S_OK;
ICluster* pCluster = NULL;

// Use the apartment-threaded model to ensure the code is thread safe.
CoInitializeEx(NULL, COINIT_APARTMENTTHREADED);

// Create the object. 
hr = CoCreateInstance( __uuidof(Cluster),
                       NULL,
                       CLSCTX_INPROC_SERVER,
                       __uuidof(ICluster),
                       reinterpret_cast<void **> (&amp;pCluster) );

if (FAILED(hr))
{
  // Handle error
}

// Before exiting, release your instance of ICluster.
pCluster->Release();

CoUninitialize();
```



To create an instance of the cluster object in C#, use the **new** keyword, as shown in the following example. Use the interface, not the class, to declare the variable.


```CSharp
ICluster cluster = new Cluster();
```



After getting an instance of the Cluster object, you need to connect to the cluster's head node. For details, see [Connecting to the Cluster](connecting-to-the-cluster.md).

## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 




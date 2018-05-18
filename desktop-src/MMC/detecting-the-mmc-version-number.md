---
title: Detecting the MMC Version Number
description: Shows how to detect the MMC version.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '361fa3d0-504f-4638-94b0-e771eff75928'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["detecting the MMC version number"]
---

# Detecting the MMC Version Number

Snap-ins built using one version of the MMC SDK might behave unpredictably if loaded in an earlier version of MMC. For example, a snap-in that uses an MMC 1.2 interface (for example, [**IColumnData**](icolumndata.md)) will not work properly if the user loads the snap-in in an MMC 1.1 console.

To ensure compatibility between snap-ins and the version of an MMC console in which they are loaded, snap-ins should implement a mechanism for detecting MMC version numbers. Beginning with MMC 2.0, snap-ins can use the [**IMMCVersionInfo**](immcversioninfo.md) interface to determine the MMC version. Prior to MMC 2.0, however, there was no MMC interface to allow a snap-in to determine the MMC version. Instead, there is a fairly straightforward workaround to achieve the same goal.

Basically, snap-ins can query for MMC interfaces introduced in different MMC versions to identify version numbers. For example, if a snap-in queries for the [**IColumnData**](icolumndata.md) interface and the query is successful (the **QueryInterface** call returns S\_OK), then the snap-in knows that it is loaded in an MMC 1.2 or later console.

Depending on whether a snap-in is a primary snap-in or an extension snap-in, the details of how it detects the MMC version number differ.

## For Primary Snap-ins

For detecting MMC version numbers, primary snap-ins must use either the [**IConsole**](iconsole2.md) interface pointer passed into their [**IComponent::Initialize**](icomponent-initialize.md) implementation, or the **IUnknown** interface pointer passed into their [**IComponentData::Initialize**](icomponentdata-initialize.md) implementation. Only these two interfaces can be used to query for the new MMC 1.2 interfaces.

The following sample implementation of a global function detects the MMC version number:


```C++
MMC_VERSION GetMMCVersion(IConsole *pConsole)
{
 
  HRESULT hr1;
  HRESULT hr2;
  MMC_VERSION mmcVersion;
 
  hr1 = pConsole->QueryInterface(IID_IConsole2, (void **)&amp;m_ipConsole2);
  hr2 = pConsole->QueryInterface(IID_IColumnData, (void **)&amp;m_ipColumnData);
 
  if (S_OK == hr1 &amp;&amp; S_OK == hr2)
      mmcVersion = MMC12;
  else
  { 
    if (S_OK == hr1 &amp;&amp; S_OK != hr2)
        mmcVersion = MMC11;
    else
        mmcVersion = MMC10;
  }
 
  return mmcVersion;
}
```



The variable mmcVersion is an enumeration of type **MMC\_VERSION**.


```C++
enum MMC_VERSION {MMC10 = 0, MMC11 = 1, MMC12 = 2};
```



The [**IConsole**](iconsole2.md) interface pointer passed into the **GetMMCVersion** function is the same one that is passed into the snap-in's [**IComponent::Initialize**](icomponent-initialize.md) implementation.

Be aware that neither the **GetMMCVersion** function nor the **MMC\_VERSION** enumeration in the preceding sample will work to identify an MMC version later than version 1.2. However, you can still use the function to identify whether the version number is 1.2 or later. That is, if the function determines that the version number is neither 1.0 nor 1.1, then it must be 1.2 or later.

## For Extension Snap-ins

Not all types of extension snap-ins need to implement [**IComponentData**](icomponentdata.md) or [**IComponent**](icomponent.md), so the workaround for primary snap-ins does not work for them. The following statements apply to extension snap-ins:

-   For extension snap-ins, there is no difference in functionality between MMC versions 1.1 and 1.2, so there is no need for an extension snap-in to detect whether it is loaded in an MMC 1.2 or later console.
-   Currently, there is no way for a non-namespace extension snap-in to detect the version of the MMC console in which it is loaded.
-   Namespace extension snap-ins receive calls to their [**IComponentData::Initialize**](icomponentdata-initialize.md) and [**IComponent::Initialize**](icomponent-initialize.md) implementations, so they can use the same technique as primary snap-ins to detect MMC version numbers.

## Related topics

<dl> <dt>

[**IMMCVersionInfo**](immcversioninfo.md)
</dt> <dt>

[MMC Versions and Redistributables](mmc-versions-and-redistributables.md)
</dt> </dl>

 

 





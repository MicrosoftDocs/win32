---
description: Developers can extend the WMI infrastructure by developing WMI providers.
ms.assetid: 87bc5d10-a5d7-444b-b823-4e1a2d63efb3
ms.tgt_platform: multiple
title: Creating WMI Providers
ms.topic: article
ms.date: 05/31/2018
---

# Creating WMI Providers

Developers can extend the WMI infrastructure by developing WMI providers. WMI providers are COM objects that implement a specified set of interfaces and, until recently, were always implemented in C++. You can now use managed languages like C# to implement WMI providers. Version 3.5 of the .NET framework introduced the WMI Provider Extensions framework that makes this possible. To learn more about creating WMI providers by using that framework, read the article, [Writing coupled WMI providers using WMI.NET Provider Extension 2.0](/previous-versions/dotnet/articles/cc268228(v=msdn.10)).

> [!Note]  
> You can also create a provider using Windows Management Infrastructure (MI), the next-generation version of WMI. For more information, see [How to Implement an MI Provider](/previous-versions/windows/desktop/wmi_v2/how-to-implement-an-mi-provider).

 

The following table describes the contents in this section.



| Topic                                                      | Description                                                                    |
|------------------------------------------------------------|--------------------------------------------------------------------------------|
| [Providing Data to WMI](providing-data-to-wmi.md)         | Provides an overview of the steps involved in creating a WMI provider.         |
| [Developing a WMI Provider](developing-a-wmi-provider.md) | Describes tasks you must perform when creating various types of WMI providers. |



 

 

 

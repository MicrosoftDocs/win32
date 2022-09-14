---
title: Designing NDF Helper Class Extensions
description: This topic is intended to provide generic guidance through the helper class extension development process.
ms.assetid: f5dbd198-7d22-4e7e-830e-6753e9f4d6c8
ms.topic: article
ms.date: 05/31/2018
---

# Designing NDF Helper Class Extensions

This topic is intended to provide generic guidance through the helper class extension development process. The guidance in this topic applies to all helper class extensions. For more specific guidance, see [Windows Filtering Platform Extensible Helper Class](windows-filtering-platform-extensible-helper-class.md) and [802.11 Wireless Diagnostics Extensible Helper Classes](802-11-wireless-diagnostics-extensible-helper-classes.md).

## Extending NDF Functionality

Windows Vista and later versions ship with a variety of helper classes already implemented that can diagnose and repair a wide range of issues. At times, however, third-party developers may wish to extend these helper classes to diagnose and resolve issues specific to their particular products and implementations.

The following Microsoft NDF helper classes are extensible.

-   [Windows Filtering Platform](windows-filtering-platform-extensible-helper-class.md)
-   [Wireless Security](802-11-wireless-diagnostics-extensible-helper-classes.md)

## Implementing a Helper Class Extension

Microsoft ships two interfaces that can be used to develop NDF helper class extensions.

The [**INetDiagHelperInfo**](/windows/desktop/api/ndhelper/nn-ndhelper-inetdiaghelperinfo) interface is called by NDF to validate that it has all required information and that it has chosen the correct helper class. It accomplishes this through the [**GetAttributeInfo**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelperinfo-getattributeinfo) method.

The [**INetDiagHelper**](/windows/desktop/api/ndhelper/nn-ndhelper-inetdiaghelper) interface is called by NDF for most of the activities that occur during the diagnostic procedure. Several of its methods are required, but others are optional for specific uses.

The required methods include [**Initialize**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-initialize) and [**GetDiagnosticsInfo**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-getdiagnosticsinfo). NDF calls **Initialize** to send key parameters to the helper class extension to initialize its instance state. **GetDiagnosticsInfo** provides an estimate of how long the diagnosis may take and whether it requires impersonation of the original user context.

Another method, [**LowHealth**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-lowhealth), is called to perform diagnosis on the network component corresponding to the helper class. [**Cancel**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-cancel) is called when NDF determines an ongoing diagnosis or repair should be stopped. [**Cleanup**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-cleanup) allows NDF to release NDF resources that the helper class extension has used since the call to [**Initialize**](/windows/desktop/api/ndhelper/nf-ndhelper-inetdiaghelper-initialize) was made.

For information on additional methods, see [**INetDiagHelper**](/windows/desktop/api/ndhelper/nn-ndhelper-inetdiaghelper).

NDF helper class extensions are used to diagnose and resolve connectivity problems associated with a specific application or component. They also validate the success or failure of a resolution attempt.

Developers considering the implementation of a helper class extension should perform the following tasks.

-   Identify user scenarios in which diagnostic and repair actions are helpful.
-   Provide resolutions to frequently encountered connectivity problems.
-   If a helper class extension is required, define a component health model used to represent the component's health state in NDF.

## Identify User Scenarios

Testing and use of an application may have already provided discernable patterns that a helper class extension may be able to diagnose and possibly repair. Application developers can use this data to determine the most important connectivity issues to address and to identify the user scenarios in which connectivity issues are likely to occur.

Determining the root cause of each problem is vital in this part of the process. This may require extensive research, but will help create software that is far easier for users and administrators to use. If a root cause is not identified, it becomes difficult or impossible to offer problem resolution using the helper class extension.

## Provide Resolutions

After a development team has identified the root causes of problems associated with their software, the next step is to identify the appropriate resolution actions for helping the user solve the problem as efficiently as possible.

Not all resolutions require that a helper class extension or automated action be created. In some cases, the team may determine that the best approach to resolving a root cause is to fix or update the component, provide additional help content for the component, or develop other strategies that provide better long-term solutions.

For problems in which an automated action is ideal, creating an NDF helper class extension is often an excellent solution.

Helper class extensions return information about root causes and repair information to users through NDF. The strings used to describe the root causes and repair information must be simple and easy for a non-technical user to understand. For more information on these strings, see [User Interface Guidelines for NDF Helper Class Extensions](user-interface-guidelines-for-ndf-helper-class-extensions.md).

## Define a Component Health Model

Software developers should define levels of "health" associated with the manageability of networking problems. A health model used to develop helper classes defines just two levels of health: healthy and unhealthy. These levels can also be applied to NDF helper class extensions.

A healthy component indicates an absence of problems. A component can be considered unhealthy because of its own problems, or because of problems occurring in other components on which it depends.



| Term                                                                                                                             | Description                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| <span id="LowHealth"></span><span id="lowhealth"></span><span id="LOWHEALTH"></span>LowHealth<br/>                         | This state indicates an unacceptable level of failures from this component, and that the component is the problem.<br/>    |
| <span id="LowHealth_Below"></span><span id="lowhealth_below"></span><span id="LOWHEALTH_BELOW"></span>LowHealth Below<br/> | This state indicates an unacceptable level of failures from a local machine component that this component depends on.<br/> |



 

When diagnosis takes place using NDF, the helper class extension is asked a series of questions to determine its state of health. If the extension responds that it is unhealthy, NDF asks clarifying questions, trying to diagnose the problem, its location, and where to look next. Each helper class must be able to answer the question of low health in order to better direct appropriate diagnostic activities.

## Related topics

<dl> <dt>

[Windows Filtering Platform Extensible Helper Class](windows-filtering-platform-extensible-helper-class.md)
</dt> <dt>

[802.11 Wireless Diagnostics Extensible Helper Classes](802-11-wireless-diagnostics-extensible-helper-classes.md)
</dt> </dl>

 

 






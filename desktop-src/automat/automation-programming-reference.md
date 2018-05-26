---
title: Automation
description: Automation (formerly called OLE Automation) enables software packages to expose their unique features to scripting tools and other applications.
ms.assetid: 75622ac1-a458-4e74-9e7f-371f8c7dbe19
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Automation

Automation (formerly called OLE Automation) enables software packages to expose their unique features to scripting tools and other applications.

Automation uses the Component Object Model (COM), but may be implemented independently from other OLE features, such as in-place activation.

While Automation runs on several platforms, the focus of this content is on applications that run on the Microsoft Windows operating system.

To get the most out of this content, you should be familiar with:

-   The Microsoft Windows programming environment.

-   The OLE protocols that are implemented through dynamic-link libraries (DLL) and used in conjunction with other Windows-based programs.

-   The Component Object Model (COM).

## In this section



| Topic                                                                                                                   | Description                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Overview of Automation](overview-of-automation.md)<br/>                                                         | Automation enables software packages to expose their unique features to scripting tools and other applications.<br/>                                                                                                                       |
| [Exposing ActiveX Objects](exposing-activex-objects.md)<br/>                                                     | Exposing objects makes them available for programmatic use by other applications and programming tools.<br/>                                                                                                                               |
| [Accessing ActiveX Objects](accessing-activex-objects.md)<br/>                                                   | To access exposed objects, you can create ActiveX clients using Visual Basic, Microsoft Visual C++, Microsoft Excel, and other applications and programming languages that support the Automation technology.<br/>                         |
| [Implementing the IDispatch Interface](implementing-the-idispatch-interface.md)<br/>                             | ActiveX or OLE objects can implement the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface for access by ActiveX clients, such as Visual Basic.<br/>                                                                                                |
| [Standard Objects and Naming Guidelines](standard-objects-and-naming-guidelines.md)<br/>                         | This section describes the standard ActiveX objects, and discusses naming guidelines for creating objects that are unique to applications, especially user-interactive applications that support a multiple-document interface (MDI).<br/> |
| [Type Libraries and the Object Description Language](type-libraries-and-the-object-description-language.md)<br/> | Type libraries enable others to use ActiveX objects you have created.<br/>                                                                                                                                                                 |
| [User-Defined Data Types](user-defined-data-types.md)<br/>                                                       | User-defined data types (UDT) are groups of related data items declared as one type of information.<br/>                                                                                                                                   |
| [IDispatch Data Types](idispatch-data-types.md)<br/>                                                             | This section contains information on data types used with the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface.<br/>                                                                                                                               |
| [ITypeInfo Data Types](itypeinfo-data-types.md)<br/>                                                             | This section contains information on data types used with the [**ITypeInfo**](/windows/previous-versions/oaidl/nn-oaidl-itypeinfo?branch=master) interface.<br/>                                                                                                                               |
| [Reference](reference.md)<br/>                                                                                   | Contains the reference content for Automation.<br/>                                                                                                                                                                                        |
| [Appendices](appendices.md)<br/>                                                                                 | Additional technical details related to Automation.<br/>                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Component Object Model (COM)](https://msdn.microsoft.com/library/windows/desktop/ms680573)
</dt> </dl>

 

 






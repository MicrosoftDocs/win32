---
title: Allocation of WinEvent IDs
description: Each WinEvent is intended to be used only for a specific purpose. Using a WinEvent for an unintended purpose can cause collisions with other applications or the operating system, which can cause the applications or operating system to become unstable.
ms.assetid: 956d6db4-f342-4b11-bfd9-92725284223f
ms.topic: article
ms.date: 05/31/2018
---

# Allocation of WinEvent IDs

Each WinEvent is intended to be used only for a specific purpose. Using a WinEvent for an unintended purpose can cause collisions with other applications or the operating system, which can cause the applications or operating system to become unstable.

Microsoft has defined several different categories of WinEvents and, for each category, has defined one or more ranges of values for use as WinEvent IDs. The Community Reserved range (0xA000—0xAFFF) is available for applications that need to define new WinEvents. Using values from this range helps reduce the risk of collisions; however, developers who create new WinEvents still need to collaborate to avoid collisions among their applications.

The following table shows the WinEvent categories and the ranges of values defined for each category.



| Category                                                | Range         | Currently in use | Comments                                                                                        |
|---------------------------------------------------------|---------------|------------------|-------------------------------------------------------------------------------------------------|
| Microsoft Active Accessibility events (System Reserved) | 0x0001-0x00FF | 0x0001-0x0020    | EVENT\_SYSTEM\_\* event IDs                                                                     |
| Microsoft Active Accessibility events (System Reserved) | 0x4001-0x40FF | 0x4001-0x4007    | EVENT\_CONSOLE\_\* event IDs                                                                    |
| UI Automation events (System Reserved)                  | 0x4E00-0x4EFF | 0x4E20-0x4E33    | UI Automation event IDs                                                                         |
| UI Automation events (System Reserved)                  | 0x7500-0x75FF | 0x7530-0x759B    | UI Automation property-changed event IDs                                                        |
| Microsoft Active Accessibility events (System Reserved) | 0x8000-0x80FF | 0x8000-0x8015    | EVENT\_OBJECT\_\* event IDs                                                                     |
| OEM Reserved                                            | 0x0101-0x01FF | 0x0101-0x0122    | IAccessible2 event IDs                                                                          |
| Community Reserved                                      | 0xA000-0xAFFF | None             | Reserved for new events defined by Accessibility Interoperability Alliance (AIA) specifications |
| ATOM                                                    | 0xC000-0xFFFF | 0xC000-0xFFFF    | Reserved for custom events allocated at runtime                                                 |



 

The following topics describe the WinEvent ranges in greater detail.

## Microsoft Active Accessibility and UI Automation Events

Five ranges of WinEvent IDs are reserved for use by Microsoft Active Accessibility and Microsoft UI Automation. The first range (0x0001—0x00FF) is reserved for system-level events, typically used for describing situations affecting all applications in the system. The second range (0x4001—0x40FF) is reserved for Windows console-specific events. The third (0x4E00—0x4EFF) and fourth ranges (0x7500—0x75FF) are for the reflection of UI Automation events. Lastly, the fifth range (0x8000—0x80FF) is for object-level events that pertain to situations specific to objects within one application.

All Microsoft Active Accessibility and UI Automation events are defined in the WinUser.h and UIAutomationClient.h header files.

## OEM Reserved Events

The OEM reserved range is open to anyone who needs to use WinEvents as a communication mechanism. Developers should define and publish event definitions along with their parameters (or also with associated object types) for event processing so that accidental collisions of event IDs can be avoided. The IAccessible2 specification uses part of the OEM reserved range.

## Community Reserved Events

The Community Reserved range is for WinEvents specified by the Accessibility Interoperability Alliance (AIA) for use across the industry. Developers are strongly encouraged to define and publish an official specification before using values from this range.

## ATOM Events

The ATOM range is reserved for event IDs that are allocated at runtime through the UI Automation extensibility API. Do not use the values from the ATOM range for any other purpose. Using the [**GlobalAddAtom**](/windows/desktop/api/winbase/nf-winbase-globaladdatoma) function with a string GUID is the recommended method of allocating WinEvents from the ATOM range.

## Using Values from a Reserved Range

According to the WinEvent specification, values from the System Reserved range, or any other non-defined range, cannot be used without revising the SDK. For new WinEvents, applications should use values from the OEM Reserved or Community Reserved ranges. Before using a new WinEvent, developers are strongly advised to share their specifications openly and widely, and should work with the Accessibility Interoperability Alliance to define WinEvent specifications.

## Related topics

<dl> <dt>

[WinEvents](winevents-infrastructure.md)
</dt> <dt>

[Accessibility Interoperability Alliance](https://www.atia.org/)
</dt> </dl>

 

 
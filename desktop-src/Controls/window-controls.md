---
title: Windows Controls
description: A control is a child window that an application uses in conjunction with another window to enable user interaction.
ms.assetid: 0a6eb481-d94e-40c5-afec-46354520f08f
ms.topic: article
ms.date: 05/31/2018
---

# Windows Controls

## Purpose

A control is a child window that an application uses in conjunction with another window to enable user interaction. Controls are most often used within dialog boxes, but they can also be used in other windows. Controls within dialog boxes provide the user with a way to type text, choose options, and initiate actions. Controls in other windows provide a variety of services, such as letting the user choose commands, view status, and view and edit text. This documentation describes the controls provided by Windows and the programming elements used to create and manipulate them.

For a list of all Windows controls, including a link to comprehensive overview and reference information for each control, see [Control Library](individual-control-info.md).

## Developer audience

Controls are designed for use by C/C++ developers and UI designers. In general, developers need a moderate level of understanding about UI programming concepts, Windows API programming, and Unicode.

## Run-time requirements

Support for controls is provided by User32.dll and Comctl32.dll. For more information, see [Common Control Versions](common-control-versions.md).

## In this section



| Topic                                                                             | Description                                                                                                                                     |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [About Common Controls](common-controls-intro.md)<br/>                     | Provides general information that is common to all controls that are supported by Comctl32.dll.<br/>                                      |
| [Control Messages](control-messages.md)<br/>                               | Explains how Windows messages are used to communicate with controls.<br/>                                                                 |
| [Custom Controls](user-controls-intro.md)<br/>                             | Describes various ways of creating custom controls. <br/>                                                                                 |
| [Subclassing Controls](subclassing-overview.md)<br/>                       | Describes a way to customize a control by changing its features or adding new ones. <br/>                                                 |
| [Custom Draw](custom-draw.md)<br/>                                         | Describes a service, provided by some controls, that applications can use to customize various aspects of the control's appearance. <br/> |
| [Security Considerations: Microsoft Windows Controls](sec-comctls.md)<br/> | Provides information about security considerations related to the Windows controls. <br/>                                                 |
| [Control Library](individual-control-info.md)<br/>                         | Provides overviews and reference information about each control supported by User32.dll and Comctl32.dll.<br/>                            |
| [General Control Reference](common-control-reference.md)<br/>              | Provides reference information about programming elements that apply to multiple controls, not just to a specific control.<br/>           |
| [Control Spy v2.0](control-spy.md)<br/>                                    | Describes Control Spy, a tool that helps developers understand common controls. <br/>                                                     |
| [Visual Styles](themes-overview.md)<br/>                                   | Describes how the appearance of controls can change depending on the visual style chosen by the user. <br/>                               |
| [Theme File Format](themesfileformat-overview.md)<br/>                     | Discusses the format of Theme (.theme) files used in Windows 7 and Windows Vista.<br/>                                                    |



 

 

 






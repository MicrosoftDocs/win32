---
title: Listening for Ribbon Events
description: The Windows Ribbon framework uses the Event Tracing for Windows (ETW) infrastructure to enable developers to learn how users are interacting with their application's ribbon.
ms.assetid: F29A8E41-C902-410E-BD28-653E078320E9
keywords:
- Windows Ribbon,events
- Ribbon,events
ms.topic: article
ms.date: 05/31/2018
---

# Listening for Ribbon Events

The Windows Ribbon framework uses the [Event Tracing for Windows (ETW)](../etw/event-tracing-portal.md) infrastructure to enable developers to learn how users are interacting with their application's ribbon.

## Introduction

The Ribbon framework event mechanism is designed such that the framework reports ribbon UI events to the application so you can monitor user activity, learn their interaction patterns, and assess usage trends. This information can be used to refine the user experience for future iterations of your ribbon app.

Using the Ribbon framework events involves the following:

1.  The ribbon application must register an [Event Tracing for Windows (ETW)](../etw/event-tracing-portal.md) listener to receive ribbon event notifications from the Ribbon framework.
2.  The Ribbon framework fires ribbon UI event callbacks at run time, if the application has registered an [Event Tracing for Windows (ETW)](../etw/event-tracing-portal.md) listener.

## Supported events

The events exposed to ribbon applications are described in the following table. 

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Event</th>
<th>Event report</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Tab activated</td>
<td>Command ID<br/> Command name<br/> Event verb<br/></td>
</tr>
<tr class="even">
<td>Contextual tab activated</td>
<td>Command ID<br/> Command name<br/> Event verb<br/></td>
</tr>
<tr class="odd">
<td>Application Menu opened</td>
<td>Event verb<br/></td>
</tr>
<tr class="even">
<td>Application Menu closed</td>
<td>Event verb<br/></td>
</tr>
<tr class="odd">
<td>Menu (regular or gallery) opened</td>
<td>Command ID<br/> Command name<br/> Event verb<br/>
<blockquote>
[!Note]<br />
QAT menu events are not exposed.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Menu (regular or gallery) closed</td>
<td>Command ID<br/> Command name<br/> Event verb<br/>
<blockquote>
[!Note]<br />
QAT menu events are not exposed.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Command</td>
<td>Command ID<br/> Command name<br/> Event verb<br/> One of the following event locations:
<ul>
<li>RIBBON</li>
<li>QUICKACCESSTOOLBAR</li>
<li>APPLICATIONMENU</li>
<li>CONTEXTPOPUP</li>
</ul>
<br/> Parent Command ID<br/> Parent Command name<br/> One of the following invoke methods:
<ul>
<li>CLICK</li>
<li>KEYTIP</li>
<li>KEYBOARD</li>
<li>TOUCH</li>
</ul>
<br/>
<blockquote>
[!Note]<br />
Item galleries and combo boxes include the selected item index but do not include string and integer values. Spinners do not include the integer value.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Ribbon minimized</td>
<td>Event verb<br/></td>
</tr>
<tr class="odd">
<td>Ribbon expanded (expand button clicked or tap pinned)</td>
<td>Event verb<br/></td>
</tr>
<tr class="even">
<td>Application mode switched</td>
<td>Event verb<br/> Mode ID (value set through <a href="https://docs.microsoft.com/windows/desktop/api/uiribbon/nf-uiribbon-iuiframework-setmodes"><strong>SetModes</strong></a>)<br/>
<blockquote>
[!Note]<br />
The application is responsible for unpacking this integer to determine which modes were set.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Tooltip displayed</td>
<td>Event verb<br/> Parent Command ID<br/> Parent Command name<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Windows Ribbon Framework Developer Guides](windowsribbon-guides-entry.md)
</dt> <dt>

[Declaring Commands and Controls with Ribbon Markup](./windowsribbon-schema.md)
</dt> <dt>

[Ribbon User Experience Guidelines](https://msdn.microsoft.com/library/cc872782.aspx)
</dt> <dt>

[Ribbon Design Process](https://msdn.microsoft.com/library/cc872781.aspx)
</dt> </dl>

 


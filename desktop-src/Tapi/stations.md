---
description: Station sets being monitored through a third-party link are modeled as a line device and possibly an associated phone device.
ms.assetid: 1d116734-cd8f-40f1-9069-2dad351a24bf
title: Stations
ms.topic: article
ms.date: 05/31/2018
---

# Stations

Station sets being monitored through a third-party link are modeled as a line device and possibly an associated phone device. The line device can have multiple addresses, if the modeled terminal supports more than one directory number (DN). Multiple call appearances on the same DN can be modeled as a single address that supports multiple calls.

Calls between two stations on the switch have two call handles, one giving the call view from the first station (on its line device), and the other giving the call view from the second station (on its line device). For example, a third-party [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) placed by an application on the server would be directed to the line device associated with the station from which the call is to be dialed; a call handle would be created on that line, on the address specified in [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams) (thereby giving control over which DN is used on a phone that supports multiple DNs). When the call is offered to the destination address, a new call handle showing a call in *offering* state is created; applications would know that it was another view of the same call by the **dwCallID** member in [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) being equal for both calls. Both calls would go *idle* when the call was dropped; a call could be dropped from the third-party application by doing a [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop) on either of the call handles.

 

 




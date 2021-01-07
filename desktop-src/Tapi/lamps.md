---
description: The lamps on a phone device can be lit in a variety of different lighting modes.
ms.assetid: d8e8ef57-9faa-4122-b99a-3956362cd9d8
title: Lamps
ms.topic: article
ms.date: 05/31/2018
---

# Lamps

The lamps on a phone device can be lit in a variety of different lighting modes. Unlike ringing patterns, lamp modes are more uniform across phone sets of different vendors. A common set of lamp modes is defined by the API. A lamp identified by its lamp-button identifier can be lit in a given lamp mode. A lamp can also be queried for its current lamp mode.

The TAPI functions used for lamps are [**phoneSetLamp**](/windows/desktop/api/Tapi/nf-tapi-phonesetlamp), which lights a lamp on a specified open phone device in a given lamp lighting mode, and [**phoneGetLamp**](/windows/desktop/api/Tapi/nf-tapi-phonegetlamp), which returns the current lamp mode of the specified lamp.

When a lamp of a phone device is changed, a [**PHONE\_STATE**](phone-state.md) message is sent to the application to notify the application about the state change. Parameters to this message provide an indication of the change.

 

 




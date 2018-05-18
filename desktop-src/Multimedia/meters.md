---
title: Meters
description: Meters
ms.assetid: '11a98d2a-7cdd-4249-bba9-7edc51d7f8b0'
keywords: ["audio mixers,controls", "audio mixers,meters", "mixers,controls", "mixers,meters", "meter controls", "MIXERCONTROLDETAILS_BOOLEAN structure", "MIXERCONTROLDETAILS_SIGNED structure", "MIXERCONTROLDETAILS_UNSIGNED structure", "Boolean control", "peak control", "signed control", "unsigned control"]
---

# Meters

The meter controls measure data passing through an audio line. These controls use the [**MIXERCONTROLDETAILS\_BOOLEAN**](mixercontroldetails-boolean.md), [**MIXERCONTROLDETAILS\_SIGNED**](mixercontroldetails-signed.md), and [**MIXERCONTROLDETAILS\_UNSIGNED**](mixercontroldetails-unsigned.md) structures to retrieve and set control properties. The following table describes the types of meters.



| Control  | Description                                                                                                                                            |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Boolean  | Measures whether an integer value is FALSE/OFF (zero) or TRUE/ON (nonzero).                                                                            |
| Peak     | Measures the deflection from 0 in both the positive and negative directions. The range of integer values for the peak meter is –32,768 through 32,767. |
| Signed   | Measures integer values in the range of –231 through (231 – 1). The mixer driver defines the limits of this meter.                                     |
| Unsigned | Measures integer values in the range of 0 through (232 – 1). The mixer driver defines the limits of this meter.                                        |



 

 

 





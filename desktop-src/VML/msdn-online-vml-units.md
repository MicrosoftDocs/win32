---
title: VML Units
description: This article describes VML units. VML is a feature that is deprecated as of Windows Internet Explorer 9.
ms.assetid: f95e65ad-d92a-460f-baeb-30fd8a35f84e
ms.topic: article
ms.date: 05/31/2018
---

# VML Units

This topic describes VML, a feature that is deprecated as of Windows Internet Explorer 9. Webpages and applications that rely on VML should be migrated to SVG or other widely supported standards.

> [!Note]  
> As of December 2011, this topic has been archived. As a result, it is no longer actively maintained. For more information, see [Archived Content](/previous-versions/windows/internet-explorer/ie-developer/). For information, recommendations, and guidance regarding the current version of Windows Internet Explorer, see [Internet Explorer Developer Center](https://msdn.microsoft.com/ie/).

 

The following CSS units are used by VML.



Relative length units

em

The height of the element's font.

ex

The height of the letter "x".

px

Pixels.

%

Percentage.

Absolute length units

in

Inches (1 inch = 2.54 centimeters ).

cm

Centimeters.

mm

Millimeters.

pt

Points (1 point = 1/72 inches ).

pc

Picas (1 pica = 12 points ).



 

Measurements and positions in cascading style sheet (CSS) properties are made using length units. Internet Explorer supports two types of length units: relative and absolute.

A relative length unit specifies a length in relation to another length property. Relative length units scale better from one output device to another, such as from a monitor to a printer. Percentages and keywords perform similarly.

An absolute length unit specifies an absolute measurement, such as inches or centimeters. Absolute length units are useful when the physical properties of the output device are known.

## Other Units of Measurement

**EMU**

The EMU (english metrical unit) is the smallest useful unit of measure and is used by VML for internal unit storage. There are 914400 EMU per inch and 12700 EMU in a point. EMUs cannot be fractional.

Since EMUs are defined by 32-bit signed integral numbers, the largest number of EMUs is 2348 inches (about 59 meters or 65 yards). Because the measurements always will fit on a screen- or page-sized output device, they will always be within this range.

**Angles**

Angle measurements can be defined with the following suffixes.



Suffix

fd

Fractional degrees.

none

Degrees

deg

Degrees

rad

Radians



 

 

 
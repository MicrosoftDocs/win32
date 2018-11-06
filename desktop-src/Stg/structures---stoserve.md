---
title: Structures - StoServe
description: COPaper packages the pen color, width, and coordinates into INKDATA structures and stores them in a dynamically allocated array that it manages in memory.
ms.assetid: 25e68c39-5306-4ad6-85dd-a8a5e256abf0
ms.topic: article
ms.date: 05/31/2018
---

# Structures - StoServe

COPaper packages the pen color, width, and coordinates into **INKDATA** structures and stores them in a dynamically allocated array that it manages in memory.

## INKDATA Structure

The following are the declarations for the **INKDATA** structure from PAPER.H.

``` syntax
// The types of Ink Data.
#define INKTYPE_NONE  0
#define INKTYPE_START 1
#define INKTYPE_DRAW  2
#define INKTYPE_STOP  3

  // The Ink Data structure.
  typedef struct _INKDATA
  {
    SHORT nType;            // Ink Type.
    SHORT nX;               // X-coordinate of ink point.
    SHORT nY;               // Y-coordinate of ink point.
    SHORT nWidth;           // Ink line width in pixels.
    COLORREF crColor;       // Ink color.
  } INKDATA;
```

The dynamic array of these **INKDATA** packets is pointed to by m\_paInkData, a member of the [**IPaper**](ipaper-methods.md) implementation class. The array is created within the **IPaper::InitPaper** method with an initial allocation. For details, see the **InitPaper** method and the private NextSlot utility method of the CImpIPaper implementation in PAPER.H. The [**InkStart**](inkstart-method.md), [**InkDraw**](inkdraw-method.md), and [**InkStop**](cguipaper-methods.md) methods use NextSlot to obtain new slots in the array. The array is expanded dynamically by NextSlot as the need arises.

The client calls the [**IPaper::Erase**](ipaper-methods.md) method to erase the current drawing. This method does not reallocate the array; it simply marks all current ink data as INKTYPE\_NONE and resets the array's end-of-data index to zero.

The client calls the [**IPaper::Lock**](ipaper-methods.md) and **Unlock** methods to manage ownership of COPaper for drawing. These methods are provided to organize access among multiple clients to the drawing held in a shared COPaper.

## PAPER\_PROPERTIES Structure

The client calls the [**IPaper::Resize**](ipaper-methods.md) method to tell COPaper that the user resized the current drawing paper rectangle. This coordinate data is kept in a **PAPER\_PROPERTIES** structure, which is stored with the ink data when all the paper data is stored in a compound file.

The following is the **PAPER\_PROPERTIES** declaration from PAPER.H.

``` syntax
#define PAPER_TITLE_SIZE 64
  typedef struct _PAPER_PROPERTIES
  {
    LONG lInkDataVersion;
    LONG lInkArraySize;
    COLORREF crWinColor;
    RECT WinRect;
    WCHAR wszTitle[PAPER_TITLE_SIZE];
    WCHAR wszAuthor[PAPER_TITLE_SIZE];
    WCHAR wszReserved1[PAPER_TITLE_SIZE];
    WCHAR wszReserved2[PAPER_TITLE_SIZE];
  } PAPER_PROPERTIES;
```

The **PAPER\_PROPERTIES** structure is designed so that new ink data formats can be added at any time as the DllPaper component evolves. The [**IPaper**](ipaper-methods.md) interface is general enough that a subsequent version of the DllPaper component may store a different ink data format while implementing the same **IPaper** interface. Because the methods of **IPaper** do not depend on a specific ink data format, a new version of the DllPaper component that does support a different ink data format can use this same interface.

The paper properties stored in a compound file record the current size of the ink data array. The proper array size can then be allocated to accommodate the ink data read from the file.

The **PAPER\_PROPERTIES** structure also stores the paper surface's drawing rectangle size and background window color.

Though not used in the **StoServe**/**StoClien** samples, a drawing title and an author name can also be stored.

Creation date and last modified dates are not included in these paper properties, because the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface used to access compound files manages this information.

 

 





---
description: Billboards can display a sequence of images and text in a dialog during an installation. Typically, billboards are used to create the visual effect of a slide show or animation that informs the user of the progress of an installation.
ms.assetid: 6432ee7d-0da2-48be-b14c-d36a83a3bb1d
title: Displaying Billboards on a Modeless Dialog
ms.topic: article
ms.date: 05/31/2018
---

# Displaying Billboards on a Modeless Dialog

Billboards can display a sequence of images and text in a dialog during an installation. Typically, billboards are used to create the visual effect of a slide show or animation that informs the user of the progress of an installation.

**To display billboards on a modeless dialog**

1.  Include a record in the [Dialog Table](dialog-table.md) for the modeless dialog box that contains the billboard. After a billboard is displayed, a modeless dialog box returns control to the Installer. This enables the Installer to process messages and update the dialog box and billboard. To create a modeless dialog box, do not set the Modal Dialog Style Bit in the Attributes field of the [Dialog Table](dialog-table.md). The following [Dialog Table](dialog-table.md) record specifies the ActionDialog dialog box.

    [Dialog Table](dialog-table.md) (partial)

    | Dialog\_     | HCentering | VCentering | Width | Height | Attributes | Title  | Control\_First | Control\_Default | Control\_Cancel |
    |--------------|------------|------------|-------|--------|------------|--------|----------------|------------------|-----------------|
    | ActionDialog | 50         | 50         | 480   | 240    | 5          | Action | Cancel         | Cancel           | Cancel          |

    

     

2.  Add a record to the [Control Table](control-table.md) to specify that the dialog box displays a billboard. The record defines the size and position of the region on the dialog box where the billboard controls listed in the [BBControl Table](bbcontrol-table.md) are to be displayed. The following [Control Table](control-table.md) record defines the position and size of the billboard on the ActionDialog dialog box.

    [Control Table](control-table.md) (partial)

    | Dialog\_     | Control   | Type      | X   | Y   | Width | Height | Attributes |
    |--------------|-----------|-----------|-----|-----|-------|--------|------------|
    | ActionDialog | Billboard | Billboard | 0   | 110 | 480   | 130    | 1          |

    

     

3.  The [Billboard Table](billboard-table.md) lists the billboard controls and specifies when a specific billboard control is displayed. Add a record to the [Billboard Table](billboard-table.md) for each billboard control. The [Billboard Table](billboard-table.md) watches for progress messages sent during an installation. A billboard is displayed only when a progress message is sent by the actions listed in the Action column of the [Billboard Table](billboard-table.md), and only if the feature in the Feature\_ field is selected for installation. After a billboard is displayed, it remains visible until covered by another billboard, or until the dialog box is closed. If multiple billboards are specified for an action, they are displayed one at a time in the order specified by the Ordering field. For example, the following [Billboard Table](billboard-table.md) entries first display the BB1 and then the BB2 [Billboard Controls](billboard-control.md) when the [InstallFiles](installfiles-action.md) action is run and the QuickTest feature has been selected to be installed.

    [Billboard Table](billboard-table.md) (partial)

    | Billboard | Feature   | Action       | Ordering |
    |-----------|-----------|--------------|----------|
    | BB1       | QuickTest | InstallFiles | 1        |
    | BB2       | QuickTest | InstallFiles | 2        |

    

     

4.  The [BBControl Table](bbcontrol-table.md) specifies the controls that belong to the [Billboard Controls](billboard-control.md) that are listed in the [Billboard Table](billboard-table.md). The [Text Control](text-control.md), [Bitmap Control](bitmap-control.md), and [Icon Control](icon-control.md) are the only types of controls that can go on a billboard. Multiple controls can be placed on each billboard. Enter the name of the billboard into the Billboard\_ field of the [BBControl Table](bbcontrol-table.md) exactly as it appears in the [Billboard Table](billboard-table.md).

    Each control position is specified as the coordinates of the upper left corner of the control. The coordinate system origin is located at the upper left corner of the billboard control rather than at a corner of the dialog box. The coordinates are in Installer units, not dialog units. An Installer unit is equal to one-twelfth the height of the 10-point MS Sans Serif font size. The following [BBControl Table](bbcontrol-table.md) records ties controls to billboards.

    [BBControl Table](bbcontrol-table.md) (partial)

    | Billboard | BBControl | Type   | X   | Y   | Width | Height | Attributes | Text             |
    |-----------|-----------|--------|-----|-----|-------|--------|------------|------------------|
    | BB1       | Text      | Text   | 100 | 30  | 280   | 280    | 3          | First Billboard  |
    | BB1       | Bitmap1   | Bitmap | 0   | 0   | 100   | 100    | 3          | Software         |
    | BB1       | Bitmap2   | Bitmap | 380 | 0   | 100   | 100    | 3          | Music            |
    | BB2       | Text      | Text   | 100 | 30  | 280   | 20     | 3          | Second Billboard |
    | BB2       | Bitmap1   | Bitmap | 0   | 0   | 100   | 100    | 3          | Music            |
    | BB2       | Bitmap2   | Bitmap | 380 | 0   | 100   | 100    | 3          | Software         |

    

     

5.  To display a billboard on the ActionDialog dialog box, you must subscribe the billboard control to [SetProgress ControlEvent](setprogress-controlevent.md) by adding a record to the [EventMapping Table](eventmapping-table.md). When the Installer publishes the SetProgress ControlEvent that is specified in the Event column, the Installer sets the control attribute that is specified in the Attribute field. The Event field contains the string identifier (without quotes) of the SetProgress ControlEvent. The Attribute field contains the string identifier (without quotes) of the attribute to be set. The Dialog\_ and Control\_ fields identify the Billboard Control and should match those fields in the [Control Table](control-table.md). For example, the following [EventMapping Table](eventmapping-table.md) subscribes a control to an event.

    [EventMapping Table](eventmapping-table.md) (partial)

    | Dialog\_     | Control\_ | Event       | Attribute |
    |--------------|-----------|-------------|-----------|
    | ActionDialog | Billboard | SetProgress | Progress  |

    

     

 

 




---
title: C
description: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Robots: noindex, nofollow
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f06e2975-569e-4b8c-9c74-15dd7b441fbf
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# C

[A](a-gly.md) [B](b-gly.md) C [D](d-gly.md) [E](e-gly.md) [F](f-gly.md) [G](g-gly.md) [H](h-gly.md) [I](i-gly.md) J K [L](l-gly.md) [M](m-gly.md) [N](n-gly.md) [O](o-gly.md) [P](p-gly.md) Q [R](r-gly.md) [S](s-gly.md) [T](t-gly.md) [U](u-gly.md) [V](v-gly.md) [W](w-gly.md) X Y Z

<dl> <dt>

<span id="mmc_clipboard_format_gly"></span><span id="MMC_CLIPBOARD_FORMAT_GLY"></span>**clipboard format**
</dt> <dd>

Format of data on the clipboard. A clipboard format is identified by a unique unsigned integer value. In MMC, clipboard formats are used for data transfer between MMC and snap-ins and between multiple snap-ins. Snap-ins register the clipboard formats that they support by using the RegisterClipboardFormat Windows API.

</dd> <dt>

<span id="mmc_clsid_class_identifier__gly"></span><span id="MMC_CLSID_CLASS_IDENTIFIER__GLY"></span>**CLSID (class identifier)**
</dt> <dd>

For COM. In MMC, a globally unique identifier (GUID) associated with a snap-in's primary object. Each snap-in (stand-alone and extension) must register its CLSID in the system registry so that MMC can locate the snap-in and load it in the console when it is required.

</dd> <dt>

<span id="mmc_code_window_gly"></span><span id="MMC_CODE_WINDOW_GLY"></span>**code window**
</dt> <dd>

Window in the Snap-in Designer for Visual Basic in which snap-in developers write code for handling events during runtime.

</dd> <dt>

<span id="mmc_column_configuration_data_gly"></span><span id="MMC_COLUMN_CONFIGURATION_DATA_GLY"></span>**column configuration data**
</dt> <dd>

Used with [*column persistence*](#mmc-column-persistence-gly). Refers to the persisted column customization and sorting parameters that MMC stores in memory when the user customizes a list view column.

</dd> <dt>

<span id="mmc_column_filtering_gly"></span><span id="MMC_COLUMN_FILTERING_GLY"></span>**column filtering**
</dt> <dd>

For MMC 1.2. A feature, in which a list view can be displayed in filtered mode.

</dd> <dt>

<span id="mmc_column_header_gly"></span><span id="MMC_COLUMN_HEADER_GLY"></span>**column header**
</dt> <dd>

Used in a Visual Basic snap-in to represent an object that defines the properties of a list view column displayed in detail or filtered mode.

</dd> <dt>

<span id="mmc_column_persistence_gly"></span><span id="MMC_COLUMN_PERSISTENCE_GLY"></span>**column persistence**
</dt> <dd>

For MMC 1.2. A feature that persists column customization and sorting parameters as the user moves between scope items in the scope pane.

MMC also allows snap-ins to view and modify persisted column customization and sorting parameters (also called [*column configuration data*](#mmc-column-configuration-data-gly)) by using the [**IColumnData**](/windows/desktop/api/Mmc/nn-mmc-icolumndata) interface.

</dd> <dt>

<span id="mmc_column_set_gly"></span><span id="MMC_COLUMN_SET_GLY"></span>**column set**
</dt> <dd>

Used with [*column persistence*](#mmc-column-persistence-gly). A set of columns inserted in the result pane by a snap-in when the user selects a scope item in the snap-in.

</dd> <dt>

<span id="mmc_column_set_id_gly"></span><span id="MMC_COLUMN_SET_ID_GLY"></span>**column set ID**
</dt> <dd>

Used with [*column persistence*](#mmc-column-persistence-gly). Uniquely identifies a column set and its [*column configuration data*](#mmc-column-configuration-data-gly). MMC persists column configuration data per column set, per view, per snap-in instance.

</dd> <dt>

<span id="mmc_completion_page_gly"></span><span id="MMC_COMPLETION_PAGE_GLY"></span>**Completion page**
</dt> <dd>

Last page of a Wizard97-style wizard. The Completion page typically has a bitmap image, called a [*watermark*](https://www.bing.com/search?q=*watermark*), to convey a specific message to the user. This is the same watermark image that is used in the Wizard97-style wizard [*Welcome page*](https://www.bing.com/search?q=*Welcome page*).

</dd> <dt>

<span id="mmc_component_object_model_com__gly"></span><span id="MMC_COMPONENT_OBJECT_MODEL_COM__GLY"></span>**Component Object Model (COM)**
</dt> <dd>

Architecture for defining interfaces and interaction among objects implemented by varying software applications. A COM object instantiates one or more interfaces, each of which exposes zero or more properties and zero or more methods. All COM interfaces are derived from the base class IUnknown. MMC is built on the COM foundation.

</dd> <dt>

<span id="mmc_composite_data_object_gly"></span><span id="MMC_COMPOSITE_DATA_OBJECT_GLY"></span>**composite data object**
</dt> <dd>

Data object created by MMC that consists of an array of [*multiselection data objects*](https://www.bing.com/search?q=*multiselection data objects*) provided by the snap-ins involved in a multiple selection operation.

</dd> <dt>

<span id="mmc_configuration_wizard_gly"></span><span id="MMC_CONFIGURATION_WIZARD_GLY"></span>**configuration wizard**
</dt> <dd>

[*Wizard*](https://www.bing.com/search?q=*Wizard*) that a snap-in can optionally display when the user adds the snap-in to a [*console*](#mmc-console-gly) using the **Add/Remove Snap-in** dialog box. The snap-in can use the wizard to gather settings for initializing the snap-in state.

</dd> <dt>

<span id="mmc_console_gly"></span><span id="MMC_CONSOLE_GLY"></span>**console**
</dt> <dd>

Instance of the MMC application as well as the main MMC window. The term "MMC" is often used interchangeably with "console" in the MMC SDK documentation. A console does not perform management functions, but it hosts tools ([*snap-ins*](https://www.bing.com/search?q=*snap-ins*)) that provide required management behavior. A console can have one or more [*multiple-document interface (MDI)*](https://www.bing.com/search?q=*multiple-document interface (MDI)*) child windows, or [*views*](https://www.bing.com/search?q=*views*) in which snap-ins are hosted.

</dd> <dt>

<span id="mmc_console_file_gly"></span><span id="MMC_CONSOLE_FILE_GLY"></span>**console file**
</dt> <dd>

File with an .msc (management saved console) extension that preserves the list of loaded snap-ins for a [*console*](#mmc-console-gly), the arrangement and contents of open [*multiple-document interface (MDI)*](https://www.bing.com/search?q=*multiple-document interface (MDI)*) child windows ([*views*](https://www.bing.com/search?q=*views*)) in the main MMC window, the default mode, and information about permissions. Configuration settings for the tools and controls are saved with the console and restored when the console file is opened.

</dd> <dt>

<span id="mmc_console_taskpad_gly"></span><span id="MMC_CONSOLE_TASKPAD_GLY"></span>**console taskpad**
</dt> <dd>

For MMC 1.2. A [*taskpad*](https://www.bing.com/search?q=*taskpad*) that can be used to run tasks such as starting wizards, opening property pages, performing menu commands, running command lines, and opening webpages. Console taskpads are implemented by MMC; this differs from standard taskpads, which are implemented by snap-ins.

</dd> <dt>

<span id="mmc_console_tree_gly"></span><span id="MMC_CONSOLE_TREE_GLY"></span>**console tree**
</dt> <dd>

Hierarchical structure in the scope pane of a [*view*](https://www.bing.com/search?q=*view*). Displays the [*static nodes*](https://www.bing.com/search?q=*static nodes*) and [*enumerated nodes*](https://www.bing.com/search?q=*enumerated nodes*) associated with stand-alone and extension snap-ins.

</dd> <dt>

<span id="mmc_container_gly"></span><span id="MMC_CONTAINER_GLY"></span>**container**
</dt> <dd>

[*Scope item*](https://www.bing.com/search?q=*Scope item*) with child scope items.

</dd> <dt>

<span id="mmc_context_menu_extension_gly"></span><span id="MMC_CONTEXT_MENU_EXTENSION_GLY"></span>**context menu extension**
</dt> <dd>

[*Extension snap-in*](https://www.bing.com/search?q=*Extension snap-in*) that extends the functionality of a [*primary snap-in*](https://www.bing.com/search?q=*primary snap-in*). The context menu extension adds menu items to the context menus of scope and result items of a particular [*node type*](https://www.bing.com/search?q=*node type*).

</dd> <dt>

<span id="mmc_control_gly"></span><span id="MMC_CONTROL_GLY"></span>**control**
</dt> <dd>

Child window that an application uses with another window to perform simple input and output (I/O) tasks. Examples of controls in the main MMC window are the [*toolbar control*](https://www.bing.com/search?q=*toolbar control*) and the [*menu button control*](https://www.bing.com/search?q=*menu button control*).

</dd> <dt>

<span id="mmc_control_bar_gly"></span><span id="MMC_CONTROL_BAR_GLY"></span>**control bar**
</dt> <dd>

A [*control*](#mmc-control-gly) implemented by MMC to display and manage its own toolbars and menu buttons, as well as those added by snap-ins.

</dd> <dt>

<span id="mmc_cookie_gly"></span><span id="MMC_COOKIE_GLY"></span>**cookie**
</dt> <dd>

In MMC, pointer-sized identifier within an instance of a snap-in that is associated with a particular scope or result item. When inserting an item in the scope or result pane, a snap-in passes to MMC the value that will be used as the item's cookie value. The value is solely determined by the snap-in.

</dd> <dt>

<span id="mmc_custom_ocx_view_gly"></span><span id="MMC_CUSTOM_OCX_VIEW_GLY"></span>**custom OCX view**
</dt> <dd>

See [*OCX view*](https://www.bing.com/search?q=*OCX view*).

</dd> <dt>

<span id="mmc_custom_taskpad_gly"></span><span id="MMC_CUSTOM_TASKPAD_GLY"></span>**custom taskpad**
</dt> <dd>

[*Taskpad*](https://www.bing.com/search?q=*Taskpad*) view style in which the snap-in displays a custom DHTML page that contains tasks as well as other elements.

</dd> <dt>

<span id="mmc_custom_web_view_gly"></span><span id="MMC_CUSTOM_WEB_VIEW_GLY"></span>**custom web view**
</dt> <dd>

See [*HTML view*](https://www.bing.com/search?q=*HTML view*).

</dd> </dl>

 

 





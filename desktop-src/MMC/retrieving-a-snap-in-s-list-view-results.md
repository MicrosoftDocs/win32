---
title: Retrieving a Snap-in's List View Results
description: Use the MMC 2.0 automation object model to manipulate MMC snap-ins.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '41da7cd2-646e-4b12-9509-bbd343be98e9'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
---

# Retrieving a Snap-in's List View Results

Use the [MMC 2.0 automation object model](mmc-2-0-automation-object-model.md) to manipulate MMC snap-ins. For example, use the MMC 2.0 automation object model to retrieve the data contained in a snap-in's list view. The following procedure show how to retrieve data from a snap-in's list view using VBScript; however, the procedure is language-independent.

**To retrieve data from a snap-in's list view**

1.  Use the CreateObject or CoCreateInstanceEx methods to get an instance of the MMC 2.0 [**Application object**](application-object.md).
2.  Use the [**Application.Load method**](application-load.md) to load an MMC console file:

    ```VB
    objMMC.Load("eventvwr.msc")
    ```

    

    The console file determines which nodes can be traversed and what data is available in the list view.

    An alternative to using Application.Load is to add a snap-in using the [**SnapIns.Add method**](snapins-add.md). Depending on the snap-in, the user could be prompted for information when a snap-in is added. The Application.Load method, however, does not require user interaction.

3.  Navigate to the proper scope node(s) using the [**Document.RootNode property**](document-rootnode.md) to navigate to the console's root node, and then use the [**ScopeNamespace.GetChild**](scopenamespace-getchild.md) method or the [**ScopeNamespace.GetNext**](scopenamespace-getnext.md) method to navigate further.
4.  Expand a node by using the [**ScopeNamespace.Expand method**](scopenamespace-expand.md), and then use the [**View.ActiveScopeNode property**](view-activescopenode.md) to specify a node as the active scope node.
5.  Use the [**View.ListItems property**](view-listitems.md) to retrieve the collection of rows (items) in the list view.

    The View.ListItems property returns a [**Nodes collection**](nodes-collection.md).

6.  Use the [**View.CellContents property**](view-cellcontents.md) to return data for a given list view item and column index:
    ```VB
    Dim str
    ' Retrieve data from the first column.
    str = objView.CellContents(objItem, 1)
    ```

    

7.  \[Optional\] Use the return data from Step 6 to examine the row (list view item) for specific data. For example, the following code determines whether the retrieved data equals "Accounts Payable":

    ```VB
    ' Determine whether the data matches my search criteria.
    If (str = "Accounts Payable") Then
        ' This row satisfies the search criteria. Use it as required.
        ' ...
    End If
    ```

    

    Or, for efficiency, you can use a console file that has already filtered the snap-in results when examining a large amount of list view data.

8.  \[Optional\] You then use the [**View.CellContents property**](view-cellcontents.md) again to output the cell contents:
    ```VB
    ' Display the contents of the first cell.
    Wscript.echo objView.CellContents(objItem, 1)
    ```

    

9.  Repeat Steps 6 through 8 for each row in the list view.

    The Nodes collection supports For Each syntax:

    ```VB
    For Each objItem In objList
        ...
    Next
    ```

    

    Alternatively, you could set up a loop based on the [**Nodes.Count property**](nodes-count.md) and [**Nodes.Item method**](nodes-item.md):

    ```VB
    Dim objItem
    Dim i
    For i = 1 To objList.Count
        Set objItem = objList.Item(i)
        ...
    Next
    ```

    

Consider using the [**View.ExportList method**](view-exportlist.md) to output all columns for a list view; the View.ExportList method does not require the script to loop through each row.

The following example uses the MMC 2.0 automation object model and the Event Viewer snap-in to make a report of all error events in the Event logs.

## Example Code \[VBScript\]


```VB
' This script makes a report of all Error events in the Event
' Viewer logs. The script uses the MMC 2.0 application object model and
' the Event Viewer snap-in.

Option Explicit

' Create the MMC Application object.
Dim objMMC
Set objMMC = Wscript.CreateObject("MMC20.Application")

' Load a console file.
' The console file in this case contains the Event Viewer snap-in.
' This console file ships with the operating system.
objMMC.Load("eventvwr.msc")
 
' Retrieve the Document object. The Document object provides access
' to the ScopeNamespace and ActiveView objects.
Dim objDoc
Set objDoc = objMMC.Document

' Retrieve the ScopeNamespace object. The ScopeNamespace object
' will be used when navigating the scope tree.
Dim objSN
Set objSN = objDoc.ScopeNamespace

' Get the console root node.
Dim objRoot
Set objRoot = objDoc.RootNode

' Using the console Root Node, get the Event Viewer node.
Dim objEvtVwrNode
Set objEvtVwrNode = objSN.GetChild(objRoot)

' Expand the Event Viewer Node.
objSN.Expand(objEvtVwrNode)

' Get the ActiveView, which is a View object.
' This object is used to access the list of nodes and column data.
Dim objView
Set objView = objDoc.ActiveView

' Get the first child node of the Event Viewer node.
On Error Resume Next
Dim objNode
Set objNode = Nothing
Set objNode = objSN.GetChild(objEvtVwrNode)
if (objNode Is Nothing) then
    ' Unexpected condition.
    Wscript.echo "Unable to get Event Viewer child node."
    Wscript.quit 
end if

Dim objSib  ' Used when moving to the next child (sibling) node.
' Loop through each Event Viewer's child nodes.
Do Until (objNode is Nothing)
    ' Expand the Event Viewer's child node.
    objSN.Expand(objNode)

    ' Display text stating which node is being examined.
    Wscript.echo "Error events in the " + objNode.Name + " log"
    Wscript.echo "====================================="

    ' Set the active scope node to the child node.
    objView.ActiveScopeNode = objNode

    ' Access the view's list of nodes.
    ' objView.ListItems represents the nodes in the list view.
    Dim objList
    Set objList = objView.ListItems

    ' Iterate through the list of nodes.
    Dim objItem
    For Each objItem In objList
        Dim str
        ' Retrieve the data in the first column. In the Event Viewer
        ' snap-in, the first column is for the Event type.
        str = objView.CellContents(objItem, 1)
        ' Determine if the event type is for an Error event.
        If (str = "Error") Then
            ' The node is for an Error event.
            ' Output the details of this Error event, with 
            ' a comma separating each data field.
            Wscript.echo objView.CellContents(objItem, 1) + ",", _
                         objView.CellContents(objItem, 2) + ",", _
                         objView.CellContents(objItem, 3) + ",", _
                         objView.CellContents(objItem, 4) + ",", _
                         objView.CellContents(objItem, 5) + ",", _
                         objView.CellContents(objItem, 6) + ",", _
                         objView.CellContents(objItem, 7) + ",", _
                         objView.CellContents(objItem, 8)
        End If
    Next

    ' Print a blank line before the next child node is processed.
    Wscript.echo ""

    ' Move to the next node under the Event Viewer node.
    Set objSib = Nothing
    Set objSib = objSN.GetNext(objNode)
    Set objNode = objSib

Loop
```



For simplicity, the script assumes that the Event Viewer node is the first child node of the Console Root node (this is the default state for Eventvwr.msc). If you do not want to make that assumption, you can update the script to examine the root node's child nodes (use the [**ScopeNamespace.GetChild method**](scopenamespace-getchild.md) and the [**ScopeNamespace.GetNext method**](scopenamespace-getnext.md)).

For brevity, the example script is hard-coded to display eight columns of data. An alternative to hard-coding is to use [**Columns collection**](columns-collection.md). The [**View.Columns property**](view-columns.md) returns the **Columns** collection for the view. Use the [**Columns.Count property**](columns-count.md) to determine the number of columns in the view. Use the [**Columns.Item method**](columns-item.md) to return a [**Column object**](column-object.md).

To use the script to examine more than one computer, you have two options. One option is to open a different MMC console file for each computer being examined. Another option is to open a single MMC console file that manages several different computers, then navigate to each Event Viewer node and process the list view. The latter option also relies on the ScopeNamespace.GetChild and ScopeNamespace.GetNext methods.

Output from the script example can be redirected to a text file. Additionally, the script can be started by the Task Scheduler, thereby requiring no user interaction. Be aware that if the script is started by the Task Scheduler, use Cscript.exe to execute the script so that message boxes are not displayed by Wscript.echo statements. For example, if the script was saved as "MyEvtErr.vbs" and the scheduled task was saved as "RunEvtEr.cmd", then the following could be used as the text in RunEvtEr.cmd.

**cscript.exe d:\\MyEvtErr.vbs //NoLogo &gt;d:\\MyOutput.txt**

## Related topics

<dl> <dt>

[MMC 2.0 Automation Object Model](mmc-2-0-automation-object-model.md)
</dt> <dt>

[Using VBScript with the MMC 2.0 automation object model](using-vbscript-with-the-mmc-2-0-automation-object-model.md)
</dt> <dt>

[**Application object**](application-object.md)
</dt> <dt>

[**Column object**](column-object.md)
</dt> <dt>

[**Columns collection**](columns-collection.md)
</dt> <dt>

[**Document object**](document-object.md)
</dt> <dt>

[**Node object**](node-object.md)
</dt> <dt>

[**Nodes collection**](nodes-collection.md)
</dt> <dt>

[**ScopeNamespace object**](scopenamespace-object.md)
</dt> <dt>

[**View object**](view-object.md)
</dt> </dl>

 

 





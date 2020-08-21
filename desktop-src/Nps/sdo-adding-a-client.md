---
title: Adding a Client
description: Adding a Client
ms.assetid: 7e9e25af-e3b9-40ba-a89d-50b3874e3e68
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Adding a Client

The following Visual Basic code adds a new RADIUS client, and sets the address and shared secret for the client.

> [!Note]  
> A COM reference must be added to the Visual Basic project in order for it to build properly. An example of the VB command sequence looks like this: Add reference -> COM -> "IAS SDO 1.0 Type Library". This varies based on your version of VB.

 

> [!Note]  
> This example does not work as VBScript code.

 


```VB
Option Explicit On 

Public Class Form1
   Inherits System.Windows.Forms.Form


#Region " Windows Form Designer generated code "

   Public Sub New()
      MyBase.New()

      'This call is required by the Windows Form Designer.
      InitializeComponent()

      'Add any initialization after the InitializeComponent() call

   End Sub

   'Form overrides dispose to clean up the component list.
   Protected Overloads Overrides Sub Dispose(ByVal disposing As Boolean)
      If disposing Then
         If Not (components Is Nothing) Then
            components.Dispose()
         End If
      End If
      MyBase.Dispose(disposing)
   End Sub

   'Required by the Windows Form Designer
   Private components As System.ComponentModel.IContainer

   'NOTE: The following procedure is required by the Windows Form Designer
   'It can be modified using the Windows Form Designer.  
   'Do not modify it using the code editor.
   Friend WithEvents Button1 As System.Windows.Forms.Button
   <System.Diagnostics.DebuggerStepThrough()> Private Sub InitializeComponent()
      Me.Button1 = New System.Windows.Forms.Button()
      Me.SuspendLayout()
      '
      'Button1
      '
      Me.Button1.Location = New System.Drawing.Point(80, 24)
      Me.Button1.Name = "Button1"
      Me.Button1.TabIndex = 0
      Me.Button1.Text = "Add Client"
      '
      'Form1
      '
      Me.AutoScaleBaseSize = New System.Drawing.Size(5, 13)
      Me.ClientSize = New System.Drawing.Size(248, 85)
      Me.Controls.AddRange(New System.Windows.Forms.Control() {Me.Button1})
      Me.Name = "Form1"
      Me.Text = "SDO Sample code: Add Client"
      Me.ResumeLayout(False)

   End Sub

#End Region

   Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
      On Error GoTo ErrorHandler ' Enable error-handling routine.

      '
      ' Attach to the local computer
      '
      Dim sdomachine As New SDOIASLib.SdoMachine()
      sdomachine.Attach(vbNullString)  'local

      '
      ' Retrieve a service SDO
      '
      Dim ServiceSdo As SDOIASLib.ISdo
      ServiceSdo = sdomachine.GetServiceSDO(SDOIASLib.IASDATASTORE.DATA_STORE_LOCAL, "IAS")

      '
      ' Retrieve the protocols collection
      '
      Dim ProtocolsCollection As SDOIASLib.ISdoCollection
      ProtocolsCollection = ServiceSdo.GetProperty(SDOIASLib.IASPROPERTIES.PROPERTY_IAS_PROTOCOLS_COLLECTION)

      '
      ' Retrieve the RADIUS protocol
      '
      Dim SdoRADIUS As SDOIASLib.ISdo
      SdoRADIUS = ProtocolsCollection.Item("Microsoft Radius Protocol")

      '
      ' Retrieve the clients collection
      '
      Dim ClientsCollection As SDOIASLib.ISdoCollection
      ClientsCollection = SdoRADIUS.GetProperty(SDOIASLib.RADIUSPROPERTIES.PROPERTY_RADIUS_CLIENTS_COLLECTION)

      Dim ClientName
      ClientName = InputBox("Enter client's name:", "Client's Name")
      If (ClientName = "") Then Exit Sub

      '
      ' Verify that the name is unique
      '
      If Not ClientsCollection.IsNameUnique(ClientName) Then
         Dim Answer
         Answer = MsgBox("Client already exists", vbExclamation + vbOKOnly, "Add client Error")
         Exit Sub
      End If

      '
      ' Add the client
      '
      Dim ClientSdo As SDOIASLib.ISdo
      Call ClientsCollection.Add(ClientName, ClientSdo)

      '
      ' Set the address for the client
      '
      Dim ClientAddress
      ClientAddress = InputBox("Enter the client's address (IP or DNS):", "Client's Address")
      Call ClientSdo.PutProperty(SDOIASLib.CLIENTPROPERTIES.PROPERTY_CLIENT_ADDRESS, ClientAddress)

      '
      ' Set the shared secret for the client
      '                                    
      Dim ClientSecret
      ClientSecret = InputBox("Enter the client's shared secret:", "Client's shared Secret")
      Call ClientSdo.PutProperty(SDOIASLib.CLIENTPROPERTIES.PROPERTY_CLIENT_SHARED_SECRET, ClientSecret)

      '
      ' Apply the changes
      '  
      Call ClientSdo.Apply()

      Exit Sub

ErrorHandler:
      ' Insert code to handle the error here
      Resume Next

   End Sub
End Class

```



## Related topics

<dl> <dt>

[**CLIENTPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-clientproperties)
</dt> <dt>

[Enumerating Objects in a Collection](/windows/desktop/Nps/sdo-enumerating-objects-in-a-collection)
</dt> <dt>

[**IASPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-iasproperties)
</dt> <dt>

[**ISdo**](/windows/desktop/api/sdoias/nn-sdoias-isdo)
</dt> <dt>

[**ISdoMachine**](/windows/desktop/api/sdoias/nn-sdoias-isdomachine)
</dt> <dt>

[**RADIUSPROPERTIES**](/windows/desktop/api/sdoias/ne-sdoias-radiusproperties)
</dt> </dl>

 

 
---
title: Adding Contact Classes
description: To programmatically extend the AD LDS schema, a user must have sufficient rights to modify the schema.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d6d2d5cf-cb35-4d9e-af6a-4522a46ce234
ms.prod: windows-server-dev
ms.technology: active-directory-application-mode
ms.tgt_platform: multiple
keywords:
- AD LDS examples ADAM , adding contact classes
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Adding Contact Classes

To programmatically extend the AD LDS schema, a user must have sufficient rights to modify the schema. To modify the schema, bind to the schema partition of an AD LDS instance, create a new object or attribute class, and set appropriate properties of the new class.

Programmatic extension of the AD LDS schema is sometimes required. Unlike using an LDIF file to extend the schema, you can make a programmatic extension invariant to change by building and supplying only an executable file.

For more information about programmatically extending the schema in Active Directory, see [Programmatic Extension](https://msdn.microsoft.com/library/ms677631).

After you extend the schema with the following code example, create **Contact** objects by [Creating Contact Objects](creating-contact-objects.md).

The following Visual Basic Scripting Edition code example binds to the schema of an AD LDS instance, creates an **attributeSchema** object for a new attribute named "Additional-Information" and sets its properties, and creates a **classSchema** object for a new class named "Contact" and sets its properties.


```VB
' Extend AD LDS Schema with the Contact Class
' and Additional-Information Attribute.

Option Explicit

' Global declarations.
Const ADS_PROPERTY_APPEND             = 3  ' Append operation.
Const DS_INSTANCETYPE_NC_IS_WRITEABLE = 4  ' Write-able attribute.
Dim objRoot                 ' Root of AD LDS instance.
Dim objSchema               ' Schema partiton.
Dim strSchemaNamingContext  ' Schema DN.

' Get schema path.
Set objRoot = GetObject("LDAP://localhost:389/RootDSE")
strSchemaNamingContext = objRoot.Get("schemaNamingContext")
Set objSchema = GetObject("LDAP://localhost:389/" & _
                    strSchemaNamingContext)

WScript.Echo "Schema path: " & objSchema.ADsPath
WScript.Echo

' Declarations for new attribute.
Const strAttributeName = "Additional-Information"  ' Attribute name.
Dim objNewAttribute                                ' New attribute.
Dim strCNAttributeName                             ' Attribute CN.

' Create new attribute.
strCNAttributeName = "CN=" & strAttributeName
Set objNewAttribute = objSchema.Create("attributeSchema", _
                          strCNAttributeName)

' Set selected values for attribute.
objNewAttribute.Put "instanceType", DS_INSTANCETYPE_NC_IS_WRITEABLE
objNewAttribute.Put "attributeID", "1.2.840.113556.1.4.265"
objNewAttribute.Put "attributeSyntax", "2.5.5.12"
objNewAttribute.Put "isSingleValued", True
objNewAttribute.Put "rangeUpper", 32768
objNewAttribute.Put "showInAdvancedViewOnly", True
objNewAttribute.Put "adminDisplayName", strAttributeName
objNewAttribute.Put "adminDescription", strAttributeName
objNewAttribute.Put "oMSyntax", 64
objNewAttribute.Put "searchFlags", 0
objNewAttribute.Put "lDAPDisplayName", "notes"
objNewAttribute.Put "name", strAttributeName
objNewAttribute.Put "systemOnly", False
objNewAttribute.Put "systemFlags", 16
objNewAttribute.Put "objectCategory", "CN=Attribute-Schema," & _
                        strSchemaNamingContext
objNewAttribute.SetInfo
WScript.Echo "Success: Created attributeSchema class object: " & _
                 objNewAttribute.Name

' Update schema cache.
WScript.Echo "         Updating the schema cache."
objRoot.Put "schemaUpdateNow", 1
objRoot.SetInfo
WScript.Echo

' Declarations for new class.
Const strClassName = "Contact"  ' Class name.
Dim objNewClass                 ' New class.
Dim strCNClassName              ' Class CN.

' Create new class.
strCNClassName = "CN=" & strClassName
Set objNewClass = objSchema.Create("classSchema", strCNClassName)

' Set selected values for class.
objNewClass.Put "instanceType", DS_INSTANCETYPE_NC_IS_WRITEABLE
objNewClass.Put "subClassOf", "organizationalPerson"
objNewClass.Put "governsID", "1.2.840.113556.1.5.15"
objNewClass.Put "rDNAttID", "cn"
objNewClass.Put "showInAdvancedViewOnly", True
objNewClass.Put "adminDisplayName", strClassName
objNewClass.Put "adminDescription", strClassName
objNewClass.Put "objectClassCategory", 1
objNewClass.Put "lDAPDisplayName", strClassName
objNewClass.Put "name", strClassName
objNewClass.Put "systemOnly", False
objNewClass.PutEx ADS_PROPERTY_APPEND, _
                "systemPossSuperiors", Array("organizationalUnit", _
                "domainDNS")
objNewClass.Put "systemMayContain", "notes"
objNewClass.Put "systemMustContain", "cn"
objNewClass.Put "defaultSecurityDescriptor", _
                "D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)" & _
                "(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)" & _
                "(A;;RPLCLORC;;;AU)"
objNewClass.Put "systemFlags", 16
objNewClass.Put "defaultHidingValue", False
objNewClass.Put "objectCategory", "CN=Class-Schema," & _
                    strSchemaNamingContext
objNewClass.Put "defaultObjectCategory", "CN=Person," & _
                    strSchemaNamingContext
objNewClass.SetInfo
WScript.Echo "Success: Created classSchema class object: " _
              & objNewClass.Name

' Update schema cache.
WScript.Echo "         Updating the schema cache."
objRoot.Put "schemaUpdateNow", 1
objRoot.SetInfo
```



The following Visual Basic .NET code example binds to the schema of an AD LDS instance, creates an **attributeSchema** object for a new attribute named "Additional-Information" and sets its properties, and creates a **classSchema** object for a new class named "Contact" and sets its properties.


```VB
Imports System
Imports System.DirectoryServices

Namespace ADAM_Examples

    Class ExtendSchemaContact

        '/ <summary>
        '/ Extend AD LDS Schema with Contact Class
        '/ and Additional-Information Attribute.
        '/ </summary>

        <STAThread()>  Shared Sub Main()

            ' Writeable attribute.
            Const DS_INSTANCETYPE_NC_IS_WRITEABLE As Integer = 4

            Dim objRoot As DirectoryEntry         ' Root of AD LDS instance.
            Dim objSchema As DirectoryEntry       ' Schema partiton.
            Dim strSchemaNamingContext As String  ' Schema DN.

            ' Get schema path.
            Try
                objRoot = New DirectoryEntry("LDAP://localhost:389/RootDSE")
                strSchemaNamingContext = objRoot.Properties( _
                    "schemaNamingContext").Value.ToString()
                objSchema = New DirectoryEntry(String.Concat( _
                    "LDAP://localhost:389/", strSchemaNamingContext))

                Console.WriteLine("Schema path: {0}", objSchema.Path)
                Console.WriteLine()
            Catch e As Exception
                Console.WriteLine("Error:   Schema bind failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Declarations for new attribute.
            '  Attribute name.
            Const strAttributeName As String = "Additional-Information"
            '  New attribute.
            Dim objNewAttribute As DirectoryEntry
            '  Attribute CN.
            Dim strCNAttributeName As String

            ' Create new attribute.
            Try
                strCNAttributeName = String.Concat("CN=", strAttributeName)
                objNewAttribute = objSchema.Children.Add( _
                    strCNAttributeName, "attributeSchema")
            Catch e As Exception
                Console.WriteLine("Error:   Attribute create failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Set selected values for attribute.
            Try
                objNewAttribute.Properties("instanceType").Add( _
                    DS_INSTANCETYPE_NC_IS_WRITEABLE)
                objNewAttribute.Properties("attributeID").Add( _
                    "1.2.840.113556.1.4.265")
                objNewAttribute.Properties("attributeSyntax").Add( _
                    "2.5.5.12")
                objNewAttribute.Properties("isSingleValued").Add(True)
                objNewAttribute.Properties("rangeUpper").Add(32768)
                objNewAttribute.Properties("showInAdvancedViewOnly").Add( _
                    True)
                objNewAttribute.Properties("adminDisplayName").Add( _
                    strAttributeName)
                objNewAttribute.Properties("adminDescription").Add( _
                    strAttributeName)
                objNewAttribute.Properties("oMSyntax").Add(64)
                objNewAttribute.Properties("searchFlags").Add(0)
                objNewAttribute.Properties("lDAPDisplayName").Add("notes")
                objNewAttribute.Properties("name").Add(strAttributeName)
                objNewAttribute.Properties("systemOnly").Add(False)
                objNewAttribute.Properties("systemFlags").Add(16)
                objNewAttribute.Properties("objectCategory").Add( _
                    String.Concat("CN=Attribute-Schema,", _
                    strSchemaNamingContext))
                objNewAttribute.CommitChanges()

                Console.WriteLine( _
                    "Success: Created attributeSchema class object:")
                Console.WriteLine("         {0}", objNewAttribute.Name)
            Catch e As Exception
                Console.WriteLine( _
                    "Error:   Setting attribute properties failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Update schema cache.
            Try
                Console.WriteLine("         Updating schema cache.")
                objRoot.Properties("schemaUpdateNow").Value = 1
                objRoot.CommitChanges()
                Console.WriteLine()
            Catch e As Exception
                Console.WriteLine("Error:   Updating schema cache failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Declarations for new class.
            Const strClassName As String = "Contact"  ' Class name.
            Dim objNewClass As DirectoryEntry         ' New class.
            Dim strCNClassName As String              ' Class CN.

            ' Create new class.
            Try
                strCNClassName = String.Concat("CN=", strClassName)
            objNewClass = objSchema.Children.Add( _
                    strCNClassName, "classSchema")
            Catch e As Exception
                Console.WriteLine("Error:   Class create failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Set selected values for class.
            Try
                objNewClass.Properties("instanceType").Add( _
                    DS_INSTANCETYPE_NC_IS_WRITEABLE)
                objNewClass.Properties("subClassOf").Add( _
                    "organizationalPerson")
                objNewClass.Properties("governsID").Add( _
                    "1.2.840.113556.1.5.15")
                objNewClass.Properties("rDNAttID").Add("cn")
                objNewClass.Properties("showInAdvancedViewOnly").Add(True)
                objNewClass.Properties("adminDisplayName").Add(strClassName)
                objNewClass.Properties("adminDescription").Add(strClassName)
                objNewClass.Properties("objectClassCategory").Add(1)
                objNewClass.Properties("lDAPDisplayName").Add(strClassName)
                objNewClass.Properties("name").Add(strClassName)
                objNewClass.Properties("systemOnly").Add(False)
                objNewClass.Properties("systemPossSuperiors").AddRange( _
                    New Object() {"organizationalUnit", "domainDNS"})
                objNewClass.Properties("systemMayContain").Add("notes")
                objNewClass.Properties("systemMustContain").Add("cn")
                objNewClass.Properties("defaultSecurityDescriptor").Add( _
                    String.Concat("D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)", _
                    "(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)", _
                    "(A;;RPLCLORC;;;AU)"))
                objNewClass.Properties("systemFlags").Add(16)
                objNewClass.Properties("defaultHidingValue").Add(False)
                objNewClass.Properties("objectCategory").Add(String.Concat( _
                    "CN=Class-Schema,", strSchemaNamingContext))
                objNewClass.Properties("defaultObjectCategory").Add( _
                    String.Concat("CN=Person,", strSchemaNamingContext))
                objNewClass.CommitChanges()

                Console.WriteLine( _
                    "Success: Created classSchema class object:")
                Console.WriteLine("         {0}", objNewClass.Name)
            Catch e As Exception
                Console.WriteLine( _
                    "Error:   Setting class properties failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            ' Update schema cache.
            Try
                Console.WriteLine("         Updating schema cache.")
                objRoot.Properties("schemaUpdateNow").Value = 1
                objRoot.CommitChanges()
            Catch e As Exception
                Console.WriteLine("Error:   Updating schema cache failed.")
                Console.WriteLine("         {0}", e.Message)
                Return
            End Try

            Return

        End Sub 'Main
    End Class 'ExtendSchemaContact
End Namespace 'ADAM_Examples
```



The following C# code example binds to the schema of an AD LDS instance, creates an **attributeSchema** object for a new attribute named "Additional-Information" and sets its properties, and creates a **classSchema** object for a new class named "Contact" and sets its properties.


```CSharp
using System;
using System.DirectoryServices;

namespace ADAM_Examples
{
    class ExtendSchemaContact
    {
        /// <summary>
        /// Extend AD LDS Schema with Contact Class
        ///  and Additional-Information Attribute.
        /// </summary>
        [STAThread]
        static void Main()
        {
            // Writeable attribute.
            const int DS_INSTANCETYPE_NC_IS_WRITEABLE = 4;

            DirectoryEntry objRoot;         // Root of AD LDS instance.
            DirectoryEntry objSchema;       // Schema partiton.
            string strSchemaNamingContext;  // Schema DN.

            // Get schema path.
            try
            {
                objRoot = new DirectoryEntry(
                    "LDAP://localhost:389/RootDSE");
                strSchemaNamingContext = objRoot.Properties[
                    "schemaNamingContext"].Value.ToString();
                objSchema = new DirectoryEntry(String.Concat(
                    "LDAP://localhost:389/", strSchemaNamingContext));

                Console.WriteLine("Schema path: {0}", objSchema.Path);
                Console.WriteLine();
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Schema bind failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Declarations for new attribute.
            // Attribute name.
            const string strAttributeName = "Additional-Information";
            // New attribute.
            DirectoryEntry objNewAttribute;
            // Attribute CN.
            string strCNAttributeName;

            // Create new attribute.
            try
            {
                strCNAttributeName = String.Concat("CN=",
                    strAttributeName);
                objNewAttribute = objSchema.Children.Add(
                    strCNAttributeName, "attributeSchema");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Attribute create failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Set selected values for attribute.
            try
            {
                objNewAttribute.Properties[
                    "instanceType"].Add(DS_INSTANCETYPE_NC_IS_WRITEABLE);
                objNewAttribute.Properties[
                    "attributeID"].Add("1.2.840.113556.1.4.265");
                objNewAttribute.Properties[
                    "attributeSyntax"].Add("2.5.5.12");
                objNewAttribute.Properties[
                    "isSingleValued"].Add(true);
                objNewAttribute.Properties["rangeUpper"].Add(32768);
                objNewAttribute.Properties[
                    "showInAdvancedViewOnly"].Add(true);
                objNewAttribute.Properties[
                    "adminDisplayName"].Add(strAttributeName);
                objNewAttribute.Properties[
                    "adminDescription"].Add(strAttributeName);
                objNewAttribute.Properties["oMSyntax"].Add(64);
                objNewAttribute.Properties["searchFlags"].Add(0);
                objNewAttribute.Properties[
                    "lDAPDisplayName"].Add("notes");
                objNewAttribute.Properties["name"].Add(strAttributeName);
                objNewAttribute.Properties["systemOnly"].Add(false);
                objNewAttribute.Properties["systemFlags"].Add(16);
                objNewAttribute.Properties["objectCategory"].Add(
                    String.Concat("CN=Attribute-Schema,",
                    strSchemaNamingContext));
                objNewAttribute.CommitChanges();

                Console.WriteLine(
                    "Success: Created attributeSchema class object:");
                Console.WriteLine("         {0}", objNewAttribute.Name);
            }
            catch (Exception e)
            {
                Console.WriteLine(
                    "Error:   Setting attribute properties failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Update schema cache.
            try
            {
                Console.WriteLine("         Updating schema cache.");
                objRoot.Properties["schemaUpdateNow"].Value = 1;
                objRoot.CommitChanges();
                Console.WriteLine();
            }
            catch (Exception e)
            {
                Console.WriteLine(
                    "Error:   Updating schema cache failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Write declarations for new class.
            const string strClassName = "Contact";  // Class name.
            DirectoryEntry objNewClass;             // New class.
            string strCNClassName;                  // Class CN.

            // Create new class.
            try
            {
                strCNClassName = String.Concat("CN=", strClassName);
                objNewClass = objSchema.Children.Add(
                    strCNClassName, "classSchema");
            }
            catch (Exception e)
            {
                Console.WriteLine("Error:   Class create failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Set selected values for class.
            try
            {
                objNewClass.Properties[
                    "instanceType"].Add(DS_INSTANCETYPE_NC_IS_WRITEABLE);
                objNewClass.Properties[
                    "subClassOf"].Add("organizationalPerson");
                objNewClass.Properties[
                    "governsID"].Add("1.2.840.113556.1.5.15");
                objNewClass.Properties["rDNAttID"].Add("cn");
                objNewClass.Properties[
                    "showInAdvancedViewOnly"].Add(true);
                objNewClass.Properties[
                    "adminDisplayName"].Add(strClassName);
                objNewClass.Properties[
                    "adminDescription"].Add(strClassName);
                objNewClass.Properties["objectClassCategory"].Add(1);
                objNewClass.Properties[
                    "lDAPDisplayName"].Add(strClassName);
                objNewClass.Properties["name"].Add(strClassName);
                objNewClass.Properties["systemOnly"].Add(false);
                objNewClass.Properties["systemPossSuperiors"].AddRange(
                    new object[] {"organizationalUnit", "domainDNS"});
                objNewClass.Properties["systemMayContain"].Add("notes");
                objNewClass.Properties["systemMustContain"].Add("cn");
                objNewClass.Properties[
                    "defaultSecurityDescriptor"].Add(String.Concat(
                    "D:(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;DA)",
                    "(A;;RPWPCRCCDCLCLORCWOWDSDDTSW;;;SY)",
                    "(A;;RPLCLORC;;;AU)"));
                objNewClass.Properties["systemFlags"].Add(16);
                objNewClass.Properties["defaultHidingValue"].Add(false);
                objNewClass.Properties["objectCategory"].Add(
                    String.Concat("CN=Class-Schema,",
                    strSchemaNamingContext));
                objNewClass.Properties["defaultObjectCategory"].Add(
                    String.Concat("CN=Person,",
                    strSchemaNamingContext));
                objNewClass.CommitChanges();

                Console.WriteLine(
                    "Success: Created classSchema class object:");
                Console.WriteLine("         {0}", objNewClass.Name);
            }
            catch (Exception e)
            {
                Console.WriteLine(
                    "Error:   Setting class properties failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }

            // Update schema cache.
            try
            {
                Console.WriteLine("         Updating schema cache.");
                objRoot.Properties["schemaUpdateNow"].Value = 1;
                objRoot.CommitChanges();
            }
            catch (Exception e)
            {
                Console.WriteLine(
                    "Error:   Updating schema cache failed.");
                Console.WriteLine("         {0}", e.Message);
                return;
            }
            
            return;
        }
    }
}
```



 

 





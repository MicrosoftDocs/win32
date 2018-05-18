---
title: DBCOMMANDTREE
description: DBCOMMANDTREE
ms.assetid: '141f1952-c1b7-4fbb-81d8-7ad3e9aa9b31'
keywords: ["DBCOMMANDTREE"]
---

# DBCOMMANDTREE

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBCOMMANDTREE** structure is the primary data structure used to represent any node in an OLE DB command tree, as described in the [Data Manipulation Operators](data-manipulation-operators.md) and Data Definition Operators section of this reference. This structure is used for each data manipulation language (DML) or data definition language (DDL) node in an OLE DB command tree.

``` syntax
typedef struct tagDBCOMMANDTREE {
  DBCOMMANDOP op;          // Operator identifier (2 bytes)
  WORD        wKind;       // Discriminator for the following union (2 bytes)
  struct tagDBCOMMANDTREE * pctFirstChild;  // Pointer to first child (4 bytes)
  struct tagDBCOMMANDTREE * pctNextSibling; // Pointer to sibling (4 bytes)
  union {  // Union directly represents fields that fit within 8 bytes.
           // Comments list DBVALUEKIND and DBTYPE corresponding to each field.
    __int64                 llValue;      // DBVALUEKIND_I8        (DBTYPE_I8)
    unsigned __int64        ullValue;     // DBVALUEKIND_UI8       (DBTYPE_UI8)
    BOOL                    fValue;       // DBVALUEKIND_BOOL      (DBTYPE_BOOL)
    unsigned char           uchValue;     // DBVALUEKIND_UI1       (DBTYPE_UI1)
    signed char             schValue;     // DBVALUEKIND_I1        (DBTYPE_I1)
    unsigned short          usValue;      // DBVALUEKIND_UI2       (DBTYPE_UI2)
    short                   sValue;       // DBVALUEKIND_I2        (DBTYPE_I2)
    LPOLESTR                pwszValue;    // DBVALUEKIND_WSTR      (DBTYPE_WSTR)
    LONG                    lValue;       // DBVALUEKIND_I4        (DBTYPE_I4)
    ULONG                   ulValue;      // DBVALUEKIND_UI4       (DBTYPE_UI4)
    float                   flValue;      // DBVALUEKIND_R4        (DBTYPE_R4)
    double                  dblValue;     // DBVALUEKIND_R8        (DBTYPE_R8)
    CY                      cyValue;      // DBVALUEKIND_CY        (DBTYPE_CY)
    DATE                    dateValue;    // DBVALUEKIND_DATE      (DBTYPE_DATE)
    DBDATE                  dbdateValue;  // DBVALUEKIND_DBDATE    (DBTYPE_DBDATE)
    DBTIME                  dbtimeValue;  // DBVALUEKIND_DBTIME    (DBTYPE_DBTIME)
    SCODE                   scodeValue;   // DBVALUEKIND_ERROR     (DBTYPE_ERROR)
    BSTR *                  pbstrValue;   // DBVALUEKIND_BSTR      (DBTYPE_BSTR)
    ICommand *              pCommand;     // DBVALUEKIND_COMMAND   (DBTYPE_IUNKNOWN)
    IDispatch *             pDispatch;    // DBVALUEKIND_IDISPATCH (DBTYPE_IDISPATCH)
    IMoniker *              pMoniker;     // DBVALUEKIND_MONIKER   (DBTYPE_MONIKER)
    IRowset *               pRowset;      // DBVALUEKIND_ROWSET    (DBTYPE_ROWSET)
    IUnknown *              pUnknown;     // DBVALUEKIND_IUNKNOWN  (DBTYPE_IUNKNOWN)
    DBBYGUID *              pdbbygdValue;     // DBVALUEKIND_BYGUID
    DBCOLUMNDESC *          pcoldescValue;    // DBVALUEKIND_COLDESC
    DBID *                  pdbidValue;       // DBVALUEKIND_ID
    DBLIKE *                pdblikeValue;     // DBVALUEKIND_LIKE
    DBCONTENT *             pdbcntntValue;    // DBVALUEKIND_CONTENT
    DBCONTENTSCOPE *        pdbcntntscpValue; // DBVALUEKIND_CONTENTSCOPE
    DBCONTENTTABLE *        pdbcntnttblValue; // DBVALUEKIND_CONTENTTABLE
    DBCONTENTVECTOR *       pdbcntntvcValue;  // DBVALUEKIND_CONTENTVECTOR
    DBCONTENTPROXIMITY *    pdbcntntproxValue;// DBVALUEKIND_CONTENTPROXIMITY
    DBGROUPINFO *           pdbgrpinfValue;   // DBVALUEKIND_GROUPINFO
    DBPARAMETER *           pdbparamValue;    // DBVALUEKIND_PARAMETER
    DBPROPSET *             pdbpropValue;     // DBVALUEKIND_PROPERTY
    DBSETFUNC *             pdbstfncValue;    // DBVALUEKIND_SETFUNC
    DBSORTINFO *            pdbsrtinfValue;   // DBVALUEKIND_SORTINFO
    DBTEXT *                pdbtxtValue;      // DBVALUEKIND_TEXT
    DBVECTOR *              pdbvectorValue;   // DBVALUEKIND_VECTOR | *
    SAFEARRAY *             parrayValue;      // DBVALUEKIND_ARRAY | *
    VARIANT *               pvarValue;        // DBVALUEKIND_VARIANT  (DBTYPE_VARIANT)
    GUID *                  pGuid;            // DBVALUEKIND_GUID     (DBTYPE_GUID)
    BYTE *                  pbValue;          // DBVALUEKIND_BYTES    (DBTYPE_BYTES)
    char *                  pzValue;          // DBVALUEKIND_STR      (DBTYPE_STR)
    DB_NUMERIC *            pdbnValue;        // DBVALUEKIND_NUMERIC  (DBTYPE_NUMERIC)
    DBTIMESTAMP *           pdbtsValue;       // DBVALUEKIND_DBTIMESTAMP (DBTYPE_DBTIMESTAMP)
    void *                  pvValue;          // a generic DBVALUEKIND_BYREF
    DBPROBABILISTIC *       pdbprobValue;     // DBVALUEKIND_PROBABILISTIC
    DBRELEVANTDOC *         pdbreldocValue;   // DBVALUEKIND_RELEVANTDOCUMENT
  } value;
  HRESULT   hrError;     // Error indicator, details in Extended Error info (4 bytes)
} DBCOMMANDTREE;
```

### Members



| Term                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="op"></span><span id="OP"></span>**op**<br/>                                                                      | A value of type [**DBCOMMANDOP**](dbcommandop.md) from the [**DBCOMMANDOPENUM**](dbcommandopenum.md) enumeration. It specifies an operator from the [Data Manipulation Operators](data-manipulation-operators.md) or the Data Definition Operators that defines the operation to take place on the associated field.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="wKind"></span><span id="wkind"></span><span id="WKIND"></span>**wKind**<br/>                                     | A value of type [**DBVALUEKIND**](dbvaluekind.md) from the [**DBVALUEKINDENUM**](dbvaluekindenum.md) enumerated type. It defines the data type of the associated union member so that the command processor knows how to interpret it. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| <span id="pctFirstChild"></span><span id="pctfirstchild"></span><span id="PCTFIRSTCHILD"></span>**pctFirstChild**<br/>     | A pointer to the **DBCOMMANDTREE** structure that represents the first child of this node of the command tree.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="pctNextSibling"></span><span id="pctnextsibling"></span><span id="PCTNEXTSIBLING"></span>**pctNextSibling**<br/> | A pointer to the **DBCOMMANDTREE** structure that represents the next child of this node of the command tree.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <span id="llvalue"></span><span id="LLVALUE"></span>**llvalue**<br/>                                                       | A union to hold the value for every data type supported by this OLE DB provider. For any union member data type that holds 8 bytes or less, the value itself is stored here. Otherwise, **llvalue** is a **pwszValue** member, a pointer to the data. <br/> A **pwszValue** member is a string; its interpretation is left to the provider. In other words, the consumer must understand the provider's method of name resolution. For command components "passed through" to another provider, it is left to the receiving provider to interpret the string.<br/> The **pMoniker** member is used for unresolved linked objects, in particular tables and functions.<br/> The **pRowset** member is used to reference a currently open rowset as input for a command. Most providers will fail if an [**IPersist**](_com_ipersist) method is invoked while the command tree refers to an open rowset.<br/> The **pCommand** member references another command object as input for a command. Most providers will fail if an [**IPersist**](_com_ipersist) method is invoked while the command tree refers to a command object that does not support monikers.<br/> |



 

### Remarks

Many operations create a binding environment. For example, a DBOP\_select operation has two inputs — a table and a Boolean predicate. (For more information on this operation, see [Operators with Two Variants for Ordered and Non-Ordered Tables](operators-with-two-variants-for-ordered-and-non-ordered-tables.md).) By virtue of the "select" operation, the table becomes the binding environment for the predicate. That means that the predicate may freely reference column names defined in the table. Note that not all bindings must come from the nearest table operation. For example, there might be multiple table operations within an "exist" expression, and any predicate may reference a column defined outside the "exist" expression. (In SQL, this is called a "correlated subquery.")

The typical size of a **DBCOMMANDTREE** structure for a node is 24 bytes. However, operators may store some specific information in the value field of the node. For programming convenience, the union field includes branches representing some common types that can fit within 8 bytes. Variable-length types are referenced via a pointer to the corresponding structure (such as [**DBTEXT**](dbtext.md)). The discriminator for the union is of type **WORD** rather than [**DBVALUEKIND**](dbvaluekind.md) so that it is possible to store node values such as DBVALUEKIND\_VECTOR \| DBVALUEKIND\_GUID, DBVALUEKIND\_BYREF \| DBVALUEKIND\_UI4, or DBVALUEKIND\_SAFEARRAY \| DBVALUEKIND\_I4.

 

 






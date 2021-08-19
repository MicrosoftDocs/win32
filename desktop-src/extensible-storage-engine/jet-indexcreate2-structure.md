---
description: "Learn more about: JET_INDEXCREATE2 Structure"
title: JET_INDEXCREATE2 Structure
TOCTitle: JET_INDEXCREATE2 Structure
ms:assetid: c574500e-8695-4f29-8e9d-6dff987af2a2
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294082(v=EXCHG.10)
ms:contentKeyID: 32765697
ms.date: 04/11/2016
ms.topic: reference
dev_langs:
- c++
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# JET_INDEXCREATE2 Structure


_**Applies to:** Windows | Windows Server_

The **JET_INDEXCREATE2** structure contains the information that is required to create an index over data in an Extensible Storage Engine (ESE) database. The structure is used by functions such as [JetCreateIndex2](./jetcreateindex2-function.md), and in structures such as [JET_TABLECREATE](./jet-tablecreate-structure.md) and [JET_TABLECREATE2](./jet-tablecreate2-structure.md).

The **JET_INDEXCREATE2** structure was introduced in the Windows 7 operating system.

```cpp
typedef struct tagJET_INDEXCREATE2 {
  unsigned long cbStruct;
  tchar* szIndexName;
  tchar* szKey;
  unsigned long cbKey;
  JET_GRBIT grbit;
  unsigned long ulDensity;
  union {
    unsigned long lcid;
    JET_UNICODEINDEX* pidxunicode;
  };
  union {
    unsigned long cbVarSegMac;
    JET_TUPLELIMITS* ptuplelimits;
  };
  JET_CONDITIONALCOLUMN* rgconditionalcolumn;
  unsigned long cConditionalColumn;
  JET_ERR err;
    unsigned long cbKeyMost;
  JET_SPACEHINTS* pSpacehints;
} JET_INDEXCREATE;
```

### Members

**cbStruct**

The size, in bytes, of this structure. Set this member to sizeof( JET_INDEXCREATE2 ).

**szIndexName**

The name of the index to create.

The name should meet the following conditions:

  - It should be less than JET_cbNameMost, not including the terminating null.

  - It must consist of the following set of characters: 0 (zero) through 9, A through Z, a through z, and all other punctuation except for "\!" (exclamation point), "," (comma), "\[" (opening bracket), and "\]" (closing bracket) — that is, ASCII characters 0x20, 0x22 through 0x2d, 0x2f through 0x5a, 0x5c, and 0x5d through 0x7f.

  - It must not begin with a space.

  - It must contain at least one non-space character.

**szKey**

A pointer to a double-null-terminated string of null-delimited tokens.

Each token is of the form "\<direction-specifier\>\<column-name\>", where direction-specification is either "+" or "-". For example, a **szKey** of "+abc\\0-def\\0+ghi\\0" will index over the three columns "abc" (in ascending order), "def" (in descending order), and "ghi" (in ascending order). In the C language, string literals have an implied **NULL** terminator, so the above string will be terminated by a double-NULL.

The number of columns specified in **szKey** must not exceed JET_ccolKeyMost (a version-dependent constant).

At least one column must be named in **szKey**.

Obsolete behavior: After the double-NULL terminator, it is possible to specify a language ID (a WORD which gets passed into MAKELCID( langid, SORT_DEFAULT ) ) as a way to specify the LCID for the index. It is illegal to specify both a language ID in **szKey** and an LCID in [JET_UNICODEINDEX](./jet-unicodeindex-structure.md) (by setting JET_bitIndexUnicode in *grbit*).

Deprecated: After the language ID, it is possible to pass **cbVarSegMac** as a **USHORT** data type. The behavior is undefined if the USHORT is set both in **szKey** and if **cbVarSegMac** is set in the structure.

**cbKey**

The length, in bytes, of **szKey**, including the two terminating nulls.

**grbit**

A group of bits that contain zero or more of the value options that are listed in the following table.


| <p>Value</p> | <p>Meaning</p> | 
|--------------|----------------|
| <p>JET_bitIndexUnique</p> | <p>Duplicate index entries (keys) are disallowed. This is enforced when <a href="gg269288(v=exchg.10).md">JetUpdate</a> is called, not when <a href="gg294137(v=exchg.10).md">JetSetColumn</a> is called.</p> | 
| <p>JET_bitIndexPrimary</p> | <p>The index is a primary (clustered) index. Every table must have exactly one primary index. If no primary index is explicitly defined over a table, the database engine will create its own primary index.</p> | 
| <p>JET_bitIndexDisallowNull</p> | <p>None of the columns over which the index is created may contain a <strong>NULL</strong> value.</p> | 
| <p>JET_bitIndexIgnoreNull</p> | <p>Do not add an index entry for a row if all of the columns being indexed are <strong>NULL</strong>.</p> | 
| <p>JET_bitIndexIgnoreAnyNull</p> | <p>Do not add an index entry for a row if any of the columns being indexed are <strong>NULL</strong>.</p> | 
| <p>JET_bitIndexIgnoreFirstNull</p> | <p>Do not add an index entry for a row if the first column being indexed is <strong>NULL</strong>.</p> | 
| <p>JET_bitIndexLazyFlush</p> | <p>Specifies that the index operations will be logged lazily.</p><p>JET_bitIndexLazyFlush does not affect the laziness of data updates. If the indexing operation is interrupted by process termination, Soft Recovery will still be able to able to get the database to a consistent state, but the index may not be present.</p> | 
| <p>JET_bitIndexEmpty</p> | <p>Do not try to build the index, because all entries would evaluate to <strong>NULL</strong>. <strong>grbit</strong> MUST also specify JET_bitIgnoreAnyNull when JET_bitIndexEmpty is passed. This is a performance enhancement. For example, if a new column is added to a table, and then an index is created over this newly added column, all the records in the table are scanned even though they are not added to the index. Specifying JET_bitIndexEmpty skips the scanning of the table, which could potentially take a long time.</p> | 
| <p>JET_bitIndexUnversioned</p> | <p>JET_bitIndexUnversioned causes index creation to be visible to other transactions. Ordinarily, a session in a transaction will not be able to see an index creation operation in another session. This flag can be useful if another transaction is likely to create the same index. The second index-create will simply fail instead of potentially causing many unnecessary database operations. The second transaction may not be able to use the index immediately. The index creation operation has to complete before it is usable. The session must not currently be in a transaction to create an index without version information.</p> | 
| <p>JET_bitIndexSortNullsHigh</p> | <p>Specifying this flag causes <strong>NULL</strong> values to be sorted after data for all columns in the index.</p> | 
| <p>JET_bitIndexUnicode</p> | <p>Specifying this flag affects the interpretation of the lcid/pidxunicde union field in the structure. Setting the bit means that the pidxunicode field actually points to a <a href="gg294097(v=exchg.10).md">JET_UNICODEINDEX</a> structure. JET_bitIndexUnicode is not required to index Unicode data. It is only needed to customize the normalization of Unicode data.</p> | 
| <p>JET_bitIndexTuples</p> | <p>Specifies that the index is a tuple index. See <a href="gg269207(v=exchg.10).md">JET_TUPLELIMITS</a> for a description of a tuple index.</p><p>The JET_bitIndexTuples value was introduced in the Windows XP operating system.</p> | 
| <p>JET_bitIndexTupleLimits</p> | <p>Specifying this flag affects the interpretation of the <strong>cbVarSegMac/ptuplelimits</strong> union field in the structure. Setting this bit means that the <strong>ptuplelimits</strong> field actually points to a <a href="gg269207(v=exchg.10).md">JET_TUPLELIMITS</a> structure to allow custom tuple index limits (implies JET_bitIndexTuples).</p><p>The <strong>JET_bitIndexTupleLimits</strong> value was introduced in the Windows Server 2003 operating system.</p> | 
| <p>JET_bitIndexCrossProduct<br />0x00004000</p> | <p>Specifying this flag for an index that has more than one key column that is a multivalued column will result in an index entry being created for each result of a cross product of all the values in those key columns. Otherwise, the index would only have one entry for each multivalue in the most significant key column that is a multivalued column and each of those index entries would use the first multivalue from any other key columns that are multi valued columns.</p><p>For example, if you specified this flag for an index over column A that has the values "red" and "blue" and over column B that has the values "1" and "2", the following index entries would be created: "red", "1"; "red", "2"; "blue", "1"; "blue", "2". Otherwise, the following index entries would be created: "red", "1"; "blue", "1".</p><p>The <strong>JET_bitIndexCrossProduct</strong> value was introduced in Windows Vista.</p> | 
| <p>JET_bitIndexKeyMost<br />0x00008000</p> | <p>Specifying this flag will cause the index to use the maximum key size specified in the <strong>cbKeyMost</strong> field in the structure. Otherwise, the index will use JET_cbKeyMost (255) as its maximum key size.</p><p>The <strong>JET_bitIndexKeyMost</strong> value was introduced in Windows Vista.</p> | 
| <p>JET_bitIndexDisallowTruncation<br />0x00010000</p> | <p>Specifying this flag will cause any update to the index that would result in a truncated key to fail with the JET_errKeyTruncated response code. Otherwise, keys will be silently truncated. For more information about key truncation, see <a href="gg269329(v=exchg.10).md">JetMakeKey</a>.</p><p>The <strong>JET_bitIndexDisallowTruncation</strong> value was introduced in Windows Vista.</p> | 



**ulDensity**

The percentage density of the initial index B+ tree. Specifying a number less than 100 uses up more space to create the index initially, but allows future growth of the index to be in place, thus avoiding internal fragmentation.

**lcid**

The locale identifier (LCID) to use when normalizing the data when the JET_bitIndexUnicode value is not specified in the *grbit* parameter. The LCID affects the normalization if the index is over Unicode columns.

**pidxunicode**

A pointer to a [JET_UNICODEINDEX](./jet-unicodeindex-structure.md) structure if the JET_bitIndexUnicode value is specified in the *grbit* parameter. This allows the user to specify custom flags that get passed to the [LCMapString](https://msdn.microsoft.com/library/dd318700\(vs.85\).aspx) function during Unicode normalization.

**cbVarSegMac**

The maximum length, in bytes, of each column to store in the index when the JET_bitIndexTupleLimits value is not specified in the *grbit* parameter.

Specifying a value of 0 (zero) for this field is equivalent to the following:

  - Specifying JET_cbPrimaryKeyMost for a primary index.

  - Specifying JET_cbSecondaryKeyMost for a secondary index.

**ptuplelimits**

A pointer to a [JET_TUPLELIMITS](./jet-tuplelimits-structure.md) structure if the JET_bitIndexTupleLimits value is specified in the *grbit* parameter.

**ptuplelimits** was introduced in Windows Server 2003.

**rgconditionalcolumn**

An optional parameter to an array of [JET_CONDITIONALCOLUMN](./jet-conditionalcolumn-structure.md) structures, which are used to specify the conditional columns in the index.

**cConditionalColumn**

The count of structures in the **rgconditionalcolumn** array.

**err**

Contains the return code for creating this index.

**cbKeyMost**

Specifies the maximum allowable size, in bytes, for keys in the index. This parameter is ignored if JET_bitIndexKeyMost is not specified in *grbit* parameter. If this parameter is set to zero, and JET_bitIndexKeyMost is specified in the *grbit* member, the calling function will fail with JET_err_InvalidDef.

The minimum supported maximum key size is JET_cbKeyMostMin (255), which is the legacy maximum key size.

The maximum key size is dependent on the database page size (JET_paramDatabasePageSize) as follows:

  - If JET_paramDatabasePageSize = 2048 then JET_cbKeyMostMin (255) \<= **cbKeyMost** \<= JET_cbKeyMost2KBytePage (500)

  - If JET_paramDatabasePageSize = 4096 then JET_cbKeyMostMin (255) \<= **cbKeyMost** \<= JET_cbKeyMost4KBytePage (1000)

  - If JET_paramDatabasePageSize = 8192 then JET_cbKeyMostMin (255) \<= **cbKeyMost** \<= JET_cbKeyMost8KBytePage (2000)

The maximum supported maximum key size for the instance can also be read from the JET_paramKeyMost system parameter.

**cbKeyMost** was introduced in Windows Vista.

**pSpacehints**

A pointer to a [JET_SPACEHINTS](./jet-spacehints-structure.md) structure.

**pSpacehints** was introduced in Windows 7.

### Remarks

ESE supports indexing over key columns containing multiple values. To use this feature, the column must be a tagged column type (JET_bitColumnTagged), and it must be flagged to have its multiple values indexed with JET_bitColumnMultiValued. In versions of Windows earlier than Windows Vista, only the first multivalued key column in the index will have its values expanded in the index. All other multivalued and tagged columns will only have their first values expanded in the index.

Assuming the following rows exist in a table (column Alpha is not multivalued, while columns Beta, Gamma, and Delta are multivalued), and an index is created as "+Alpha\\0+Beta\\0+Gamma\\0+Delta\\0\\0":


| <p>Alpha</p> | <p>Beta</p> | <p>Gamma</p> | <p>Delta</p> | 
|--------------|-------------|--------------|--------------|
| <p>1</p> | <p>ABC<br />GHI<br />JKL</p> | <p>MNO<br />PQR<br />STU</p> | <p>VWX<br />YZ</p> | 
| <p>2</p> | <p>THE</p> | <p>RAIN<br />SPAIN</p> | <p>IN<br />FALLS</p> | 



The following index-tuples will be stored:

{1,ABC,MNO,VWX}  
{1,GHI,MNO,VWX}  
{1,JKL,MNO,VWX}  
{2,THE,RAIN,IN}

Note that {2,THE,SPAIN,IN} is not stored, even though the Alpha column in the second row happens to have a single multivalue.

In versions of Windows starting with Windows Vista, all multivalued columns can be expanded in the index by specifying JET_bitIndexCrossProduct.

### Requirements


| 
|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 
| <p><strong>Unicode</strong></p> | <p>Implemented as <strong>JET_ INDEXCREATE2_W</strong> (Unicode) and <strong>JET_ INDEXCREATE2_A</strong> (ANSI).</p> | 



### See also

[JET_COLTYP](./jet-coltyp.md)  
[JET_CONDITIONALCOLUMN](./jet-conditionalcolumn-structure.md)  
[JET_ERR](./jet-err.md)  
[JET_GRBIT](./jet-grbit.md)  
[JET_TABLECREATE](./jet-tablecreate-structure.md)  
[JET_TABLECREATE2](./jet-tablecreate2-structure.md)  
[JET_TUPLELIMITS](./jet-tuplelimits-structure.md)  
[JET_UNICODEINDEX](./jet-unicodeindex-structure.md)  
[JetCreateIndex2](./jetcreateindex2-function.md)  
[JetSetColumn](./jetsetcolumn-function.md)  
[JetUpdate](./jetupdate-function.md)

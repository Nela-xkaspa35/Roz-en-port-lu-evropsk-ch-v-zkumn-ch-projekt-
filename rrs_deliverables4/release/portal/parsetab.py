
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xb4&\x8e\xaa\xde\x9aX\x06\x96\xb9:\xd8\xe6K\xb0\x85'
    
_lr_action_items = {'REVERSE_SOLIDUS':([5,],[12,]),'UNESCAPED':([0,2,3,4,6,9,10,11,12,13,14,15,],[2,-10,2,-8,2,-9,-11,-13,-12,2,2,2,]),'SPEC_SEPARATOR':([2,3,4,5,8,9,10,11,12,17,],[-10,-6,-8,11,15,-9,-11,-13,-12,-7,]),'ESCAPE':([0,2,3,4,6,9,10,11,12,13,14,15,],[5,-10,5,-8,5,-9,-11,-13,-12,5,5,5,]),'QUOTATION_MARK':([0,2,4,5,9,10,11,12,13,14,15,],[6,-10,-8,10,-9,-11,-13,-12,17,6,6,]),'ELEM_SEPARATOR':([1,2,3,4,7,8,9,10,11,12,16,17,18,19,],[-1,-10,-6,-8,14,-4,-9,-11,-13,-12,-3,-7,-2,-5,]),'$end':([1,2,3,4,7,8,9,10,11,12,16,17,18,19,],[-1,-10,-6,-8,0,-4,-9,-11,-13,-12,-3,-7,-2,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'qelem':([0,14,],[1,18,]),'spec_opt':([8,],[16,]),'chars':([0,6,14,15,],[3,13,3,3,]),'char':([0,3,6,13,14,15,],[4,9,4,9,4,4,]),'query':([0,],[7,]),'string':([0,14,15,],[8,8,19,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> query","S'",1,None,None,None),
  ('query -> qelem','query',1,'p_query','/home/ibp/dev/release/src/portal/query.py',187),
  ('query -> query ELEM_SEPARATOR qelem','query',3,'p_query','/home/ibp/dev/release/src/portal/query.py',188),
  ('qelem -> string spec_opt','qelem',2,'p_qelem','/home/ibp/dev/release/src/portal/query.py',198),
  ('spec_opt -> <empty>','spec_opt',0,'p_spec_opt','/home/ibp/dev/release/src/portal/query.py',205),
  ('spec_opt -> SPEC_SEPARATOR string','spec_opt',2,'p_spec_opt','/home/ibp/dev/release/src/portal/query.py',206),
  ('string -> chars','string',1,'p_string','/home/ibp/dev/release/src/portal/query.py',216),
  ('string -> QUOTATION_MARK chars QUOTATION_MARK','string',3,'p_string','/home/ibp/dev/release/src/portal/query.py',217),
  ('chars -> char','chars',1,'p_chars','/home/ibp/dev/release/src/portal/query.py',227),
  ('chars -> chars char','chars',2,'p_chars','/home/ibp/dev/release/src/portal/query.py',228),
  ('char -> UNESCAPED','char',1,'p_char','/home/ibp/dev/release/src/portal/query.py',238),
  ('char -> ESCAPE QUOTATION_MARK','char',2,'p_char','/home/ibp/dev/release/src/portal/query.py',239),
  ('char -> ESCAPE REVERSE_SOLIDUS','char',2,'p_char','/home/ibp/dev/release/src/portal/query.py',240),
  ('char -> ESCAPE SPEC_SEPARATOR','char',2,'p_char','/home/ibp/dev/release/src/portal/query.py',241),
]
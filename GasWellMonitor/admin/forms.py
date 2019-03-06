# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, ValidationError, EqualTo
from GasWellMonitor.Model import Stationinfo, Producetype, Plateinfo, Gaswellinfo, Devicestate, Devicetype, Role, Auth, \
    Alarminfo, Loginfo

stationinfo = Stationinfo.query.all()
plateinfo = Plateinfo.query.all()
producetype = Producetype.query.all()
gaswellinfo = Gaswellinfo.query.all()
devicestate = Devicestate.query.all()
devicetype = Devicetype.query.all()
role = Role.query.all()
auth_list = Auth.query.all()
station = Stationinfo.query.all()
alarminfo = Alarminfo.query.all()
logtype = Loginfo.query.all()

# 报警类型
ch = [(v.ID, v.ALARMSTATMENT) for v in alarminfo]
ch.append((0, "选择报警类型"))
ch.sort()
# 设备类型
typech = [(v.ID, v.NAME) for v in devicetype]
typech.append((0, "选择设备类型"))
typech.sort()
# 设备状态
statech = [(v.ID, v.NAME) for v in devicestate]
statech.append((0, "选择设备状态"))
statech.sort()
# 日志类型
logtypech = [(v.ID, v.LOGSTATMENT) for v in logtype]
logtypech.append((0, "选择日志类型"))
logtypech.sort()


# 站区表单
class stationForm(FlaskForm):
    name = StringField(
        label="站区名称",
        validators=[
            DataRequired("请输入站区名称！")
        ],
        description="站区",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入站区名称！"
        }
    )
    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 平台表单
class plateForm(FlaskForm):
    name = StringField(
        label="平台名称",
        validators=[
            DataRequired("请输入平台名称！")
        ],
        description="平台",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入平台名称！"
        }
    )
    gaswellnum = StringField(
        label="井口数量",
        validators=[
            DataRequired("请输入井口数量！")
        ],
        description="井口数量",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入井口数量！"
        }
    )
    stationid = SelectField(
        label="站区",
        validators=[
            DataRequired("请选择站区！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in stationinfo],
        description="站区",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )
    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 排采类型表单
class producetypeForm(FlaskForm):
    name = StringField(
        label="排采方式名称",
        validators=[
            DataRequired("请输入排采方式名称！")
        ],
        description="排采方式名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入排采方式名称！"
        }
    )
    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 井信息表单
class gaswellForm(FlaskForm):
    name = StringField(
        label="井名",
        validators=[
            DataRequired("请输入井名！")
        ],
        description="井名",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入井名！"
        }
    )

    usedate = StringField(
        label="投产时间",
        validators=[
            DataRequired("请输入投产时间！")
        ],
        description="投产时间",
        render_kw={
            "class": "form-control",
            "id": "input_release_time",
            "placeholder": "请输入投产时间！",
        }
    )

    coalnum = StringField(
        label="煤层号",
        description="煤层号",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入煤层号！"
        }
    )

    coaldepth = StringField(
        label="煤层中深(垂深)",
        description="煤层中深(垂深)",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入煤层中深(垂深)！"
        }
    )

    layer = StringField(
        label="层位",
        description="层位",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入层位！"
        }
    )

    model = StringField(
        label="排采设备型号",
        validators=[
            DataRequired("请输入排采设备型号！")
        ],
        description="排采设备型号",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入排采设备型号！"
        }
    )

    pumpdiameter = StringField(
        label="泵径",
        validators=[
            DataRequired("请输入泵径！")
        ],
        description="泵径",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入泵径！"
        }
    )

    pumpdepth = StringField(
        label="泵深",
        validators=[
            DataRequired("请输入泵深！")
        ],
        description="泵深",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入泵深！"
        }
    )

    pressuregagedepth = StringField(
        label="井下压力计（斜深）",
        description="井下压力计（斜深）",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入井下压力计（斜深）！"
        }
    )

    perforationsection = StringField(
        label="射孔井段",
        validators=[
            DataRequired("请输入射孔井段！")
        ],
        description="射孔井段",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入射孔井段！"
        }
    )

    remarks = TextAreaField(
        label="备注",
        description="备注",
        render_kw={
            "class": "form-control",
            "rows": 10,
            "id": "input_info",
        }
    )

    producemode = SelectField(
        label="排采类型",
        validators=[
            DataRequired("请选择排采类型！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in producetype],
        description="排采类型",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    pressuregagehd = StringField(
        label="井下压力计（垂深）",
        description="井下压力计（垂深）",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入井下压力计（垂深）！"
        }
    )

    plateinfoid = SelectField(
        label="平台",
        validators=[
            DataRequired("请选择平台！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in plateinfo],
        description="平台",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    gaswellallname = StringField(
        label="井全名",
        validators=[
            DataRequired("请输井全名！")
        ],
        description="井全名",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入井全名！"
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 设备类型表单
class devicetypeForm(FlaskForm):
    name = StringField(
        label="添加设备类型名称",
        validators=[
            DataRequired("请输入设备类型名称！")
        ],
        description="设备类型名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入设备类型名称！"
        }
    )

    kepware = StringField(
        label="添加KEPWARE关键字",
        validators=[
            DataRequired("请输入KEPWARE关键字！")
        ],
        description="KEPWARE关键字",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入KEPWARE关键字！"
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 设备类型表单
class devicestateForm(FlaskForm):
    name = StringField(
        label="添加设备类型名称",
        validators=[
            DataRequired("请输入设备状态名称！")
        ],
        description="设备状态名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入设备状态名称！"
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 设备信息表单
class deviceForm(FlaskForm):
    platename = SelectField(
        label="平台名",
        validators=[
            DataRequired("请选择平台名！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in plateinfo],
        description="平台名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "plateSelect",
        }
    )

    name = SelectField(
        label="井名",
        validators=[
            DataRequired("请输入井名！")
        ],
        coerce=int,
        choices=[(v.ID, v.GASWELLALLNAME) for v in gaswellinfo],
        description="井名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "gaswellSelect",
        }
    )

    type = SelectField(
        label="设备类型",
        validators=[
            DataRequired("请输入设备类型！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in devicetype],
        description="设备类型",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    brand = StringField(
        label="设备品牌",
        description="设备品牌",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入设备品牌！"
        }
    )

    model = StringField(
        label="设备型号参数",
        description="设备型号参数",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入设备型号参数！"
        }
    )

    installdate = StringField(
        label="设备安装时间",
        description="设备安装时间",
        render_kw={
            "class": "form-control",
            "id": "input_release_time",
            "placeholder": "请输设备安装时间！"
        }
    )

    state = SelectField(
        label="设备状态",
        validators=[
            DataRequired("请选择设备状态！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in devicestate],
        description="设备状态",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    remarks = TextAreaField(
        label="备注",
        description="备注",
        render_kw={
            "class": "form-control",
            "rows": 10,
            "id": "input_info",
        }
    )

    iswarning = SelectField(
        label="预警状态",
        coerce=int,
        choices=[(0, "否"), (1, "是")],
        description="预警状态",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 权限信息
class authForm(FlaskForm):
    name = StringField(
        label="权限名称",
        validators=[
            DataRequired("请输入权限名称！")
        ],
        description="权限名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入权限名称！"
        }
    )

    stationid = SelectField(
        label="站区",
        validators=[
            DataRequired("请选择可看站区！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in station],
        description="站区列表",
        render_kw={
            "class": "form-control",
            "placeholder": "请输选择可看站区！",
            "style": "text-align:center;"
        }
    )

    iswrite = SelectField(
        label="控制权限",
        coerce=int,
        choices=[(0, "否"), (1, "是")],
        description="控制权限",
        render_kw={
            "class": "form-control",
            "placeholder": "请输选择是否可控制！",
            "style": "text-align:center;"
        }
    )

    remarks = TextAreaField(
        label="备注",
        description="备注",
        render_kw={
            "class": "form-control",
            "rows": 10,
            "id": "input_info",
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 角色信息
class roleForm(FlaskForm):
    name = StringField(
        label="角色名称",
        validators=[
            DataRequired("请输入角色名称！")
        ],
        description="角色名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入角色名称！"
        }
    )

    authid = SelectMultipleField(
        label="用户权限（按住CTRL多选）",
        validators=[
            DataRequired("请选择用户权限！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in auth_list],
        description="用户权限",
        render_kw={
            "class": "form-control",
            "placeholder": "请输选择用户权限！"
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 用户信息表单
class userForm(FlaskForm):
    name = StringField(
        label="用户名称",
        validators=[
            DataRequired("请输入用户名称！")
        ],
        description="用户名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户名称！"
        }
    )

    pwd = PasswordField(
        label="用户密码",
        validators=[
            DataRequired("请输入用户密码！")
        ],
        description="用户密码",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户密码！"
        }
    )

    isadmin = SelectField(
        label="管理员权限",
        coerce=int,
        choices=[(0, "普通用户"), (1, "管理员"), (2, "领导")],
        description="管理员权限",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    email = StringField(
        label="用户邮箱",
        description="用户邮箱",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户邮箱！"
        }
    )

    phone = StringField(
        label="用户手机",
        description="用户手机",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户手机！"
        }
    )

    role_id = SelectField(
        label="所属权限",
        validators=[
            DataRequired("请选择权限！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in devicestate],
        description="所属权限",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    default = SelectField(
        label="井名",
        validators=[
            DataRequired("请选择井名！")
        ],
        coerce=int,
        choices=[(v.ID, v.GASWELLALLNAME) for v in gaswellinfo],
        description="井名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 用户编辑信息表单
class usereditForm(FlaskForm):
    name = StringField(
        label="用户名称",
        validators=[
            DataRequired("请输入用户名称！")
        ],
        description="用户名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户名称！"
        }
    )

    new_pwd = PasswordField(
        label="用户新密码",
        description="用户新密码",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户新密码！"
        }
    )

    isadmin = SelectField(
        label="管理员权限",
        coerce=int,
        choices=[(0, "普通用户"), (1, "管理员"), (2, "领导")],
        description="管理员权限",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    email = StringField(
        label="用户邮箱",
        description="用户邮箱",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户邮箱！"
        }
    )

    phone = StringField(
        label="用户手机",
        description="用户手机",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户手机！"
        }
    )

    role_id = SelectField(
        label="所属权限",
        validators=[
            DataRequired("请选择权限！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in devicestate],
        description="所属权限",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    default = SelectField(
        label="井名",
        validators=[
            DataRequired("请选择井名！")
        ],
        coerce=int,
        choices=[(v.ID, v.GASWELLALLNAME) for v in gaswellinfo],
        description="井名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


# 用户权限编辑信息表单
class userauthForm(FlaskForm):
    name = StringField(
        label="用户名称",
        validators=[
            DataRequired("请输入用户名称！")
        ],
        description="用户名称",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户名称！"
        }
    )

    pwd = PasswordField(
        label="管理员密码",
        validators=[
            DataRequired("请输入管理员密码！")
        ],
        description="管理员密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员密码！",
        }
    )

    repwd = PasswordField(
        label="管理员重复密码",
        validators=[
            DataRequired("请输入管理员重复密码！"),
            EqualTo('pwd', message="两次密码不一致!")
        ],
        description="管理员重复密码",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入管理员重复密码！",
        }
    )

    station = SelectMultipleField(
        label="用户可查看站区（按住CTRL多选）",
        validators=[
            DataRequired("请选择可查看站区！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in station],
        description="用户可查看站区",
        render_kw={
            "class": "form-control",
            "placeholder": "请选择可查看站区！"
        }
    )

    iswriteable = SelectField(
        label="页面编辑权限",
        coerce=int,
        choices=[(0, "不可编辑"), (1, "可编辑")],
        description="页面编辑权限",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    isadmin = SelectField(
        label="管理员权限",
        coerce=int,
        choices=[(0, "普通用户"), (1, "管理员")],
        description="管理员权限",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    sex = StringField(
        label="用户性别",
        description="用户性别",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "请输入用户性别！"
        }
    )

    nation = StringField(
        label="用户民族",
        description="用户民族",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "用户民族！"
        }
    )

    birthday = StringField(
        label="用户生日",
        description="用户生日",
        render_kw={
            "class": "form-control",
            "id": "birthday",
            "placeholder": "用户生日！"
        }
    )

    native = StringField(
        label="用户籍贯",
        description="用户籍贯",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "用户籍贯！"
        }
    )

    political = StringField(
        label="用户政治面貌",
        description="用户政治面貌",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "用户政治面貌！"
        }
    )

    entername = StringField(
        label="APP用户名",
        description="APP用户名",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "APP用户名！"
        }
    )

    aduser = StringField(
        label="域用户名",
        description="域用户名",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "域用户名！"
        }
    )

    idcode = StringField(
        label="用户省份证",
        description="用户省份证",
        render_kw={
            "class": "form-control",
            "id": "input_name",
            "placeholder": "用户身份证！"
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-primary"
        }
    )


class impGaswellForm(FlaskForm):
    platename = SelectField(
        label="平台名",
        validators=[
            DataRequired("请选择平台名！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in plateinfo],
        description="平台名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "plateSelect",
        }
    )

    gaswellname = SelectField(
        label="井名",
        validators=[
            DataRequired("请选择井名！")
        ],
        coerce=int,
        choices=[(v.ID, v.GASWELLALLNAME) for v in gaswellinfo],
        description="井名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "gaswellSelect",
        }
    )

    note = TextAreaField(
        label="井况描述",
        description="井况描述",
        validators=[
            DataRequired("请输入井况信息！")
        ],
        render_kw={
            "class": "form-control",
            "rows": 10,
            "id": "input_info",
        }
    )

    enddate = StringField(
        label="结束时间",
        validators=[
            DataRequired("请输入结束时间！")
        ],
        description="结束时间",
        render_kw={
            "class": "form-control",
            "id": "input_enddate",
            "placeholder": "请输入结束时间！",
        }
    )

    submit = SubmitField(
        "编辑",
        render_kw={
            "class": "btn btn-success",
        }
    )


class alarmlistForm(FlaskForm):
    state = SelectField(
        label="处理状态",
        coerce=int,
        choices=[(-1, "请选择状态"), (0, "未处理"), (1, "已处理")],
        description="处理状态",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "statSelect",
        }
    )

    alarmtype = SelectField(
        label="报警类型",
        coerce=int,
        choices=ch,
        description="报警类型",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "alarmtypeSelect",
        }
    )

    gaswellname = StringField(
        label="井名",
        description="请输入井名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入井名！",
        }
    )

    alarmuser = StringField(
        label="处理用户",
        description="请输入用户",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户！",
        }
    )

    time = StringField(
        label="报警时间段",
        description="请选择时间段",
        render_kw={
            "class": "form-control",
            "id": "alarmTime",
            "placeholder": "请选择时间段！",
        }
    )

    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-sm btn-primary",
            "id": "alarmQuery",
        }
    )


class loglistForm(FlaskForm):
    state = SelectField(
        label="日志类型",
        coerce=int,
        choices=[(-1, "请选择状态"), (0, "未处理"), (1, "已处理")],
        description="处理状态",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "statSelect",
        }
    )

    alarmtype = SelectField(
        label="报警类型",
        coerce=int,
        choices=ch,
        description="报警类型",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "alarmtypeSelect",
        }
    )

    gaswellname = StringField(
        label="井名",
        description="请输入井名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入井名！",
        }
    )

    alarmuser = StringField(
        label="处理用户",
        description="请输入用户",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户！",
        }
    )

    time = StringField(
        label="报警时间段",
        description="请选择时间段",
        render_kw={
            "class": "form-control",
            "id": "alarmTime",
            "placeholder": "请选择时间段！",
        }
    )

    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-sm btn-primary",
            "id": "alarmQuery",
        }
    )


class userauthsearchForm(FlaskForm):
    authuser = StringField(
        label="用户查询",
        description="请输入用户",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户！",
        }
    )

    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-sm btn-primary",
        }
    )


class devicesearchForm(FlaskForm):
    devicetypesearch = SelectField(
        label="设备类型",
        coerce=int,
        choices=typech,
        description="设备类型",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    devicestatesearch = SelectField(
        label="设备状态",
        coerce=int,
        choices=statech,
        description="设备状态",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    iswarningsearch = SelectField(
        label="预警状态",
        coerce=int,
        choices=[(-1, "选择状态"), (0, "否"), (1, " 是")],
        description="预警状态",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    devicegaswellsearch = StringField(
        label="井名查询",
        description="井名查询",
        render_kw={
            "class": "form-control",
            "placeholder": "井名查询！",
        }
    )

    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-sm btn-primary",
        }
    )


class opeartingwellForm(FlaskForm):
    platename = SelectField(
        label="平台名",
        validators=[
            DataRequired("请选择平台名！")
        ],
        coerce=int,
        choices=[(v.ID, v.NAME) for v in plateinfo],
        description="平台名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "plateSelect",
        }
    )

    gaswellname = SelectField(
        label="井名",
        validators=[
            DataRequired("请选择井名！")
        ],
        coerce=int,
        choices=[(v.ID, v.GASWELLALLNAME) for v in gaswellinfo],
        description="井名",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
            "id": "gaswellSelect",
        }
    )

    workteam = StringField(
        label="作业队",
        description="作业队",
        render_kw={
            "class": "form-control",
            "placeholder": "作业队！",
        }
    )

    starttime = StringField(
        label="作业开始时间",
        description="作业开始时间",
        render_kw={
            "class": "form-control",
            "placeholder": "作业开始时间！",
            "id": "workstarttime",
        }
    )

    endtime = StringField(
        label="作业结束时间",
        description="作业结束时间",
        validators=[
            DataRequired("请选择结束时间！")
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "作业结束时间！",
            "id": "workendtime",
        }
    )

    remarks = TextAreaField(
        label="备注",
        description="备注",
        render_kw={
            "class": "form-control",
            "rows": 10,
            "id": "input_info",
        }
    )

    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-sm btn-primary",
        }
    )


class logSearchForm(FlaskForm):
    logtypesearch = SelectField(
        label="日志类型",
        validators=[
            DataRequired("请选择日志类型！")
        ],
        coerce=int,
        choices=logtypech,
        description="日志类型",
        render_kw={
            "class": "form-control",
            "style": "text-align:center;",
        }
    )

    logsearchgaswellname = StringField(
        label="井名",
        description="井名",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入井名！",
        }
    )

    logusersearch = StringField(
        label="用户名",
        description="用户名",
        render_kw={
            "class": "form-control",
            "placeholder": "用户名！",
        }
    )

    tagsearch = StringField(
        label="修改内容",
        description="修改内容",
        render_kw={
            "class": "form-control",
            "placeholder": "修改内容！",
        }
    )

    submit = SubmitField(
        "查询",
        render_kw={
            "class": "btn btn-sm btn-primary",
        }
    )

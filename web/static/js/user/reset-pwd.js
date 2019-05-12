var mod_pwd_ops = {
  init: function() {
    this.eventBind();
  },

  eventBind: function() {
    $("#save").click(function() {
      var btn_target = $(this);
      if (btn_target.hasClass("disabled")) {
        common_ops.alert("请不要重复提交");
        return;
      }

      var old_password = $("#old_password").val();
      var new_password = $("#new_password").val();

      var old_password_target = $(
        ".user_reset_pwd_wrap input[id=old_password]"
      );
      var new_password_target = $(
        ".user_reset_pwd_wrap input[id=new_password]"
      );

      if (!old_password) {
        common_ops.tip("旧密码不正确~~", old_password_target);
        return false;
      }

      if (!new_password || old_password.length < 6) {
        common_ops.tip(
          "新密码不符合规范,请输入不少于6位的新密码~~",
          new_password_target
        );
        return false;
      }

      btn_target.addClass("disabled");
      var data = {
        old_password: old_password,
        new_password: new_password
      };

      $.ajax({
        url: common_ops.buildUrl("/user/reset-pwd"),
        type: "POST",
        data: data,
        dataType: "json",
        success: function(res) {
          btn_target.removeClass("disabled");
          var callback = null;
          if (res.code == 200) {
            callback = function() {
              window.location.href = window.location.href;
            };
          }
          common_ops.alert(res.msg, callback);
        }
      });
    });
  }
};

$(document).ready(function() {
  mod_pwd_ops.init();
});

$(function() {
  var createIssueApp = new Vue({delimiters: ["{(", ")}"],
  'el': '#create-issue-app',data: {'isSaved': false, 'title': '', 'description': ''},
methods:{
  save: function() {
    $.post('/api/create_issue', {title: this.title, description: this.description}, function(data) {
      createIssueApp.isSaved = true;
      createIssueApp.title = '';
      createIssueApp.description = '';

    });
  }
}})
var issueApp = new Vue({delimiters: ["{(", ")}"],
'el': '#issue-app',data: {'isSaved': false, 'title': '', 'description': '', 'new_comment': ''},
methods:{
save: function() {
  $.post('/api/create_issue', {title: this.title, description: this.description}, function(data) {
    createIssueApp.isSaved = true;
    createIssueApp.title = '';
    createIssueApp.description = '';

  });
}, saveComment:function() {
  $.post('/api/save_comment', {issue_uuid: issueUuid, comment: this.new_comment}, function(data) {
    issueApp.new_comment = '';

  });
}
}})
})

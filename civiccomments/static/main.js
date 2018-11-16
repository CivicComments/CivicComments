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
})

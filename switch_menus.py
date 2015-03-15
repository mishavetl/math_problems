def hide_options(self):
    self.apply.hide()
    self.options_menu.hide()
    self.label.hide()
    self.label1.hide()
    self.from_field.hide()
    self.to_field.hide()

def hide_menu(self):
    self.start.hide()
    self.quit.hide()
    self.options.hide()
    self.freespace.hide()
    self.freespace1.hide()

def hide_start(self):
    self.start_menu.hide()
    self.answer_field.hide()
    self.user_answer_field.hide()
    self.problem_field.hide()
    self.submit.hide()
    self.show_answer.hide()


def show_menu(self):
    self.grid.setSpacing(40)

    self.start.show()
    self.quit.show()
    self.options.show()
    self.freespace.show()
    self.freespace1.show()

def show_start(self):
    self.grid.setSpacing(40)

    self.start_menu.show()
    self.answer_field.show()
    self.user_answer_field.show()
    self.problem_field.show()
    self.submit.show()
    self.show_answer.show()

def show_options(self):
    self.grid.setSpacing(10)
    self.apply.show()
    self.options_menu.show()
    self.label.show()
    self.label1.show()
    self.from_field.show()
    self.to_field.show()

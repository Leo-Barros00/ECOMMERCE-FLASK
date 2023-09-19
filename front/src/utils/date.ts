import { format } from 'date-fns';

export function formatDateTime(date: Date) {
  console.log({ date });
  return format(date, 'dd/MM/yyyy hh:mm');
}
